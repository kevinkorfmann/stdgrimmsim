"""
Prior distributions over species parameters for training-data generation.

Each species has LogNormal or LogUniform priors over six parameters:
generation_time, population_size, mutation_rate, recombination_rate,
time_scale (multiplier for demographic event times), and migration_scale
(multiplier for migration rates).  Priors are centred on the species'
point estimate with cluster-aware spread.

Usage::

    import stdgrimmsim
    import numpy as np

    species = stdgrimmsim.get_species("ZweBerg")
    model   = species.get_demographic_model("BlackForest_1D12")
    engine  = stdgrimmsim.get_engine("msprime")
    prior   = stdgrimmsim.get_prior("ZweBerg")
    rng     = np.random.default_rng(42)

    # Single draw — includes all six parameters
    params = prior.sample(rng)

    # Rescale the demographic model with sampled Ne and time scales
    demography = prior.rescale_demography(model, params)

    # Build a contig with sampled mutation/recombination rates
    contig = prior.build_contig(species, params, length=100_000)

    # Simulate
    ts = engine.simulate(
        demography, contig,
        samples={"BlackForest": 20}, seed=rng.integers(2**31),
    )

    # Batch pipeline
    for _ in range(1000):
        params = prior.sample(rng)
        demography = prior.rescale_demography(model, params)
        contig = prior.build_contig(species, params, length=100_000)
        ts = engine.simulate(demography, contig,
                             samples={"BlackForest": 20},
                             seed=rng.integers(2**31))
"""

import copy
import math

import numpy as np


class LogNormalPrior:
    """LogNormal prior with given median and log-space standard deviation."""

    def __init__(self, median, sigma):
        self.median = median
        self.sigma = sigma

    def sample(self, rng, size=None):
        mu_log = math.log(self.median)
        return rng.lognormal(mu_log, self.sigma, size=size)

    def __repr__(self):
        return f"LogNormalPrior(median={self.median:.4g}, sigma={self.sigma})"


class LogUniformPrior:
    """LogUniform prior on [low, high]."""

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def sample(self, rng, size=None):
        log_low = math.log(self.low)
        log_high = math.log(self.high)
        u = rng.uniform(log_low, log_high, size=size)
        return np.exp(u)

    def __repr__(self):
        return f"LogUniformPrior(low={self.low:.4g}, high={self.high:.4g})"


def _rescale_demography(demography, ne_scale, time_scale, migration_scale):
    """Return a deep copy of an msprime.Demography with rescaled parameters.

    Parameters
    ----------
    demography : msprime.Demography
        The original demography object.
    ne_scale : float
        Multiplicative factor for all population sizes.
    time_scale : float
        Multiplicative factor for all event times.
    migration_scale : float
        Multiplicative factor for all migration rates.

    Returns
    -------
    msprime.Demography
        A new Demography with rescaled parameters.
    """
    import msprime

    d = copy.deepcopy(demography)

    # Scale population initial sizes
    for pop in d.populations:
        if pop.initial_size is not None:
            pop.initial_size *= ne_scale

    # Scale migration matrix
    if d.migration_matrix is not None:
        d.migration_matrix = d.migration_matrix * migration_scale

    # Scale events
    for ev in d.events:
        # Scale time on all events
        if hasattr(ev, "time") and ev.time is not None:
            ev.time *= time_scale

        # Scale population sizes in PopulationParametersChange
        if isinstance(ev, msprime.PopulationParametersChange):
            if ev.initial_size is not None:
                ev.initial_size *= ne_scale

        # Scale migration rates in MigrationRateChange
        if isinstance(ev, msprime.MigrationRateChange):
            if ev.rate is not None:
                ev.rate *= migration_scale

    return d


class PriorConfig:
    """Prior configuration for a single species.

    Holds priors over six parameters: generation_time, population_size,
    mutation_rate, recombination_rate, time_scale, and migration_scale.
    """

    def __init__(self, species_id, cluster, generation_time, population_size,
                 mutation_rate, recombination_rate, time_scale,
                 migration_scale):
        self.species_id = species_id
        self.cluster = cluster
        self.generation_time = generation_time
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.recombination_rate = recombination_rate
        self.time_scale = time_scale
        self.migration_scale = migration_scale

    def sample(self, rng, size=None):
        """Sample parameters from the prior.

        Parameters
        ----------
        rng : numpy.random.Generator
            Random number generator (e.g. ``np.random.default_rng(42)``).
        size : int, optional
            Number of samples.  If None, returns scalar values.

        Returns
        -------
        dict
            Keys: ``generation_time``, ``population_size``,
            ``mutation_rate``, ``recombination_rate``,
            ``time_scale``, ``migration_scale``.
            Values are floats (if size is None) or numpy arrays.
        """
        return {
            "generation_time": self.generation_time.sample(rng, size),
            "population_size": self.population_size.sample(rng, size),
            "mutation_rate": self.mutation_rate.sample(rng, size),
            "recombination_rate": self.recombination_rate.sample(rng, size),
            "time_scale": self.time_scale.sample(rng, size),
            "migration_scale": self.migration_scale.sample(rng, size),
        }

    def rescale_demography(self, demographic_model, params):
        """Return a rescaled DemographicModel from sampled parameters.

        Scales all population sizes by ``params["population_size"] /
        species_Ne``, all event times by ``params["time_scale"]``, and
        all migration rates by ``params["migration_scale"]``.

        Parameters
        ----------
        demographic_model : DemographicModel
            A demographic model from the catalog (e.g. from
            ``species.get_demographic_model(...)``).
        params : dict
            Output of :meth:`sample` (must be a scalar draw, not batched).

        Returns
        -------
        DemographicModel
            A copy with rescaled demography, usable with
            ``engine.simulate()``.
        """
        from . import get_species

        sp = get_species(self.species_id)
        ne_scale = params["population_size"] / sp.population_size
        rescaled_msp = _rescale_demography(
            demographic_model.model,
            ne_scale=ne_scale,
            time_scale=params["time_scale"],
            migration_scale=params["migration_scale"],
        )
        dm_copy = copy.copy(demographic_model)
        dm_copy.model = rescaled_msp
        return dm_copy

    def build_contig(self, species, params, length):
        """Build a contig with sampled mutation and recombination rates.

        Parameters
        ----------
        species : Species
            The species object.
        params : dict
            Output of :meth:`sample`.
        length : int
            Contig length in base pairs.

        Returns
        -------
        Contig
        """
        return species.get_contig(
            length=length,
            mutation_rate=params["mutation_rate"],
            recombination_rate=params["recombination_rate"],
        )

    def __repr__(self):
        return (
            f"PriorConfig(species_id={self.species_id!r}, "
            f"cluster={self.cluster!r})"
        )


# ── Cluster assignments ──────────────────────────────────────────────
# Cluster A: Ancient/Primordial   (8 species) — high r, very low μ
# Cluster B: Elemental/Aquatic    (8 species) — moderate r-dominated
# Cluster C: Woodland/Regional    (8 species) — approximately balanced
# Cluster D: Domestic/Human-adj.  (8 species) — μ-dominated

_CLUSTERS = {
    "A": [
        "LinDra", "WilJae", "ValKri", "DraFeu",
        "OstBal", "JotRie", "RueHar", "BasRex",
    ],
    "B": [
        "HexWal", "ErlKoe", "LorRhe", "PomBal",
        "MasLak", "FeeFlu", "NixRhe", "FraHol",
    ],
    "C": [
        "SaxErz", "SieRab", "MooBay", "MueGei",
        "RumSti", "ZweBerg", "SchWar", "BerAlp",
    ],
    "D": [
        "WerWol", "AscPut", "BreSta", "PukPru",
        "WolBay", "AlpNac", "HeiCol", "KobHau",
    ],
}

# σ values per cluster:  (g, Ne, μ, r, time_scale, migration_scale)
_SIGMA = {
    "A": (0.3, 0.3, 0.5, 0.5, 0.3, 0.5),
    "B": (0.3, 0.3, 0.4, 0.4, 0.3, 0.5),
    "C": (0.3, 0.3, 0.3, 0.3, 0.3, 0.5),
    "D": (0.3, 0.3, 0.3, 0.3, 0.3, 0.5),
}

# Reverse lookup: species_id → cluster letter
_SPECIES_TO_CLUSTER = {}
for _cluster, _ids in _CLUSTERS.items():
    for _sid in _ids:
        _SPECIES_TO_CLUSTER[_sid] = _cluster


def get_prior(species_id):
    """Return the PriorConfig for a species.

    Parameters
    ----------
    species_id : str
        Species identifier (e.g. ``"ZweBerg"``).

    Returns
    -------
    PriorConfig
    """
    from . import get_species

    if species_id not in _SPECIES_TO_CLUSTER:
        raise ValueError(
            f"Unknown species {species_id!r}. "
            f"Known species: {sorted(_SPECIES_TO_CLUSTER)}"
        )

    cluster = _SPECIES_TO_CLUSTER[species_id]
    sig_g, sig_ne, sig_mu, sig_r, sig_t, sig_m = _SIGMA[cluster]

    sp = get_species(species_id)
    chroms = [c for c in sp.genome.chromosomes if "mito" not in c.id]
    mu_est = chroms[0].mutation_rate
    r_est = chroms[0].recombination_rate

    return PriorConfig(
        species_id=species_id,
        cluster=cluster,
        generation_time=LogNormalPrior(sp.generation_time, sig_g),
        population_size=LogNormalPrior(sp.population_size, sig_ne),
        mutation_rate=LogNormalPrior(mu_est, sig_mu),
        recombination_rate=LogNormalPrior(r_est, sig_r),
        time_scale=LogNormalPrior(1.0, sig_t),
        migration_scale=LogNormalPrior(1.0, sig_m),
    )
