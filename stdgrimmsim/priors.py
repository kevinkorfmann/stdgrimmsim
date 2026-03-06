"""
Prior distributions over species parameters for training-data generation.

Each species has LogNormal or LogUniform priors over four parameters:
generation_time, population_size, mutation_rate, and recombination_rate.
Priors are centred on the species' point estimate with cluster-aware spread.

Usage::

    import stdgrimmsim
    import numpy as np

    prior = stdgrimmsim.get_prior("ZweBerg")
    rng = np.random.default_rng(42)

    # Single draw
    params = prior.sample(rng)
    # params["generation_time"]  -> float
    # params["population_size"]  -> float
    # params["mutation_rate"]    -> float
    # params["recombination_rate"] -> float

    # Multiple draws
    params = prior.sample(rng, size=1000)
    # params["generation_time"]  -> np.array of shape (1000,)
"""

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


class PriorConfig:
    """Prior configuration for a single species."""

    def __init__(self, species_id, cluster, generation_time, population_size,
                 mutation_rate, recombination_rate):
        self.species_id = species_id
        self.cluster = cluster
        self.generation_time = generation_time
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.recombination_rate = recombination_rate

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
            ``mutation_rate``, ``recombination_rate``.
            Values are floats (if size is None) or numpy arrays.
        """
        return {
            "generation_time": self.generation_time.sample(rng, size),
            "population_size": self.population_size.sample(rng, size),
            "mutation_rate": self.mutation_rate.sample(rng, size),
            "recombination_rate": self.recombination_rate.sample(rng, size),
        }

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

# σ values per cluster:  (g, Ne, μ, r)
_SIGMA = {
    "A": (0.3, 0.3, 0.5, 0.5),
    "B": (0.3, 0.3, 0.4, 0.4),
    "C": (0.3, 0.3, 0.3, 0.3),
    "D": (0.3, 0.3, 0.3, 0.3),
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
    sig_g, sig_ne, sig_mu, sig_r = _SIGMA[cluster]

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
    )
