"""Tests for the prior sampling system."""

import numpy as np
import pytest

import stdgrimmsim
from stdgrimmsim.priors import (
    LogNormalPrior,
    LogUniformPrior,
    PriorConfig,
    _CLUSTERS,
    _SPECIES_TO_CLUSTER,
    _rescale_demography,
)


class TestLogNormalPrior:
    def test_sample_scalar(self):
        prior = LogNormalPrior(median=100, sigma=0.3)
        rng = np.random.default_rng(42)
        val = prior.sample(rng)
        assert isinstance(val, float)
        assert val > 0

    def test_sample_array(self):
        prior = LogNormalPrior(median=100, sigma=0.3)
        rng = np.random.default_rng(42)
        vals = prior.sample(rng, size=1000)
        assert vals.shape == (1000,)
        assert np.all(vals > 0)

    def test_median_close(self):
        prior = LogNormalPrior(median=100, sigma=0.3)
        rng = np.random.default_rng(42)
        vals = prior.sample(rng, size=100_000)
        assert abs(np.median(vals) - 100) < 5

    def test_repr(self):
        prior = LogNormalPrior(median=100, sigma=0.3)
        assert "100" in repr(prior)
        assert "0.3" in repr(prior)


class TestLogUniformPrior:
    def test_sample_in_range(self):
        prior = LogUniformPrior(low=1, high=100)
        rng = np.random.default_rng(42)
        vals = prior.sample(rng, size=10_000)
        assert np.all(vals >= 1)
        assert np.all(vals <= 100)

    def test_sample_scalar(self):
        prior = LogUniformPrior(low=1, high=100)
        rng = np.random.default_rng(42)
        val = prior.sample(rng)
        assert isinstance(val, float)
        assert 1 <= val <= 100

    def test_repr(self):
        prior = LogUniformPrior(low=1, high=100)
        assert "1" in repr(prior)
        assert "100" in repr(prior)


class TestPriorConfig:
    def test_sample_returns_all_keys(self):
        config = PriorConfig(
            species_id="test", cluster="C",
            generation_time=LogNormalPrior(25, 0.3),
            population_size=LogNormalPrior(80000, 0.3),
            mutation_rate=LogNormalPrior(2.5e-8, 0.3),
            recombination_rate=LogNormalPrior(5e-8, 0.3),
            time_scale=LogNormalPrior(1.0, 0.3),
            migration_scale=LogNormalPrior(1.0, 0.5),
        )
        rng = np.random.default_rng(42)
        params = config.sample(rng)
        assert set(params.keys()) == {
            "generation_time", "population_size",
            "mutation_rate", "recombination_rate",
            "time_scale", "migration_scale",
        }
        for v in params.values():
            assert isinstance(v, float)
            assert v > 0

    def test_sample_array(self):
        config = PriorConfig(
            species_id="test", cluster="C",
            generation_time=LogNormalPrior(25, 0.3),
            population_size=LogNormalPrior(80000, 0.3),
            mutation_rate=LogNormalPrior(2.5e-8, 0.3),
            recombination_rate=LogNormalPrior(5e-8, 0.3),
            time_scale=LogNormalPrior(1.0, 0.3),
            migration_scale=LogNormalPrior(1.0, 0.5),
        )
        rng = np.random.default_rng(42)
        params = config.sample(rng, size=100)
        for v in params.values():
            assert v.shape == (100,)


class TestClusterAssignments:
    def test_all_species_assigned(self):
        catalog_ids = {sp.id for sp in stdgrimmsim.all_species()}
        assigned_ids = set(_SPECIES_TO_CLUSTER.keys())
        assert catalog_ids == assigned_ids

    def test_cluster_sizes(self):
        assert len(_CLUSTERS["A"]) == 8
        assert len(_CLUSTERS["B"]) == 8
        assert len(_CLUSTERS["C"]) == 8
        assert len(_CLUSTERS["D"]) == 8

    def test_no_duplicates(self):
        all_ids = []
        for ids in _CLUSTERS.values():
            all_ids.extend(ids)
        assert len(all_ids) == len(set(all_ids))

    def test_total_species_count(self):
        total = sum(len(ids) for ids in _CLUSTERS.values())
        assert total == 32


class TestGetPrior:
    def test_all_species(self):
        for sp in stdgrimmsim.all_species():
            prior = stdgrimmsim.get_prior(sp.id)
            assert prior.species_id == sp.id
            assert prior.cluster in ("A", "B", "C", "D")

    def test_unknown_species_raises(self):
        with pytest.raises(ValueError, match="Unknown species"):
            stdgrimmsim.get_prior("NonExistent")

    def test_point_estimates_match_species(self):
        for sp in stdgrimmsim.all_species():
            prior = stdgrimmsim.get_prior(sp.id)
            assert prior.generation_time.median == sp.generation_time
            assert prior.population_size.median == sp.population_size

    def test_cluster_a_wider_rate_sigma(self):
        prior = stdgrimmsim.get_prior("LinDra")
        assert prior.cluster == "A"
        assert prior.mutation_rate.sigma == 0.5
        assert prior.recombination_rate.sigma == 0.5

    def test_cluster_c_narrower_sigma(self):
        prior = stdgrimmsim.get_prior("ZweBerg")
        assert prior.cluster == "C"
        assert prior.generation_time.sigma == 0.3
        assert prior.mutation_rate.sigma == 0.3

    def test_has_time_and_migration_scale(self):
        prior = stdgrimmsim.get_prior("ZweBerg")
        assert prior.time_scale.median == 1.0
        assert prior.migration_scale.median == 1.0
        rng = np.random.default_rng(42)
        params = prior.sample(rng)
        assert "time_scale" in params
        assert "migration_scale" in params

    def test_reproducibility(self):
        prior = stdgrimmsim.get_prior("ZweBerg")
        p1 = prior.sample(np.random.default_rng(123))
        p2 = prior.sample(np.random.default_rng(123))
        for k in p1:
            assert p1[k] == p2[k]


class TestRescaleDemography:
    def test_rescale_ne(self):
        import msprime
        d = msprime.Demography()
        d.add_population(name="A", initial_size=1000)
        d.add_population_parameters_change(time=100, initial_size=500, population="A")
        d2 = _rescale_demography(d, ne_scale=2.0, time_scale=1.0, migration_scale=1.0)
        assert d2.populations[0].initial_size == 2000
        assert d2.events[0].initial_size == 1000
        # Original unchanged
        assert d.populations[0].initial_size == 1000

    def test_rescale_time(self):
        import msprime
        d = msprime.Demography()
        d.add_population(name="A", initial_size=1000)
        d.add_population_parameters_change(time=100, initial_size=500, population="A")
        d2 = _rescale_demography(d, ne_scale=1.0, time_scale=3.0, migration_scale=1.0)
        assert d2.events[0].time == 300
        assert d2.populations[0].initial_size == 1000  # Ne unchanged

    def test_rescale_migration(self):
        import msprime
        d = msprime.Demography()
        d.add_population(name="A", initial_size=1000)
        d.add_population(name="B", initial_size=1000)
        d.set_migration_rate(source="A", dest="B", rate=1e-4)
        d2 = _rescale_demography(d, ne_scale=1.0, time_scale=1.0, migration_scale=0.5)
        assert d2.migration_matrix[0][1] == pytest.approx(5e-5)


class TestEndToEnd:
    """Test the full pipeline: sample -> rescale -> simulate."""

    def test_1pop_simulation(self):
        import warnings
        warnings.filterwarnings("ignore")
        species = stdgrimmsim.get_species("ZweBerg")
        model = species.get_demographic_model("BlackForest_1D12")
        engine = stdgrimmsim.get_engine("msprime")
        prior = stdgrimmsim.get_prior("ZweBerg")
        rng = np.random.default_rng(42)

        params = prior.sample(rng)
        dm = prior.rescale_demography(model, params)
        contig = prior.build_contig(species, params, length=10_000)
        ts = engine.simulate(dm, contig, samples={"BlackForest": 5},
                             seed=rng.integers(2**31))
        assert ts.num_trees > 0
        assert ts.num_samples == 10  # 5 diploids = 10 haplotypes

    def test_2pop_simulation(self):
        import warnings
        warnings.filterwarnings("ignore")
        species = stdgrimmsim.get_species("ZweBerg")
        model = species.get_demographic_model("HarzBlackForest_2D12")
        engine = stdgrimmsim.get_engine("msprime")
        prior = stdgrimmsim.get_prior("ZweBerg")
        rng = np.random.default_rng(42)

        params = prior.sample(rng)
        dm = prior.rescale_demography(model, params)
        contig = prior.build_contig(species, params, length=10_000)
        ts = engine.simulate(dm, contig,
                             samples={"BlackForest": 5, "Harz": 5},
                             seed=rng.integers(2**31))
        assert ts.num_trees > 0
        assert ts.num_samples == 20

    def test_multiple_draws_vary(self):
        """Different draws should produce different tree sequences."""
        import warnings
        warnings.filterwarnings("ignore")
        species = stdgrimmsim.get_species("ZweBerg")
        model = species.get_demographic_model("BlackForest_1D12")
        engine = stdgrimmsim.get_engine("msprime")
        prior = stdgrimmsim.get_prior("ZweBerg")
        rng = np.random.default_rng(42)

        mutation_counts = []
        for _ in range(5):
            params = prior.sample(rng)
            dm = prior.rescale_demography(model, params)
            contig = prior.build_contig(species, params, length=10_000)
            ts = engine.simulate(dm, contig, samples={"BlackForest": 5},
                                 seed=rng.integers(2**31))
            mutation_counts.append(ts.num_mutations)

        # With different priors, mutation counts should vary
        assert len(set(mutation_counts)) > 1
