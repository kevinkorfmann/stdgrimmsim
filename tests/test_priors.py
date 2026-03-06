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
            species_id="test",
            cluster="C",
            generation_time=LogNormalPrior(25, 0.3),
            population_size=LogNormalPrior(80000, 0.3),
            mutation_rate=LogNormalPrior(2.5e-8, 0.3),
            recombination_rate=LogNormalPrior(5e-8, 0.3),
        )
        rng = np.random.default_rng(42)
        params = config.sample(rng)
        assert set(params.keys()) == {
            "generation_time", "population_size",
            "mutation_rate", "recombination_rate",
        }
        for v in params.values():
            assert isinstance(v, float)
            assert v > 0

    def test_sample_array(self):
        config = PriorConfig(
            species_id="test",
            cluster="C",
            generation_time=LogNormalPrior(25, 0.3),
            population_size=LogNormalPrior(80000, 0.3),
            mutation_rate=LogNormalPrior(2.5e-8, 0.3),
            recombination_rate=LogNormalPrior(5e-8, 0.3),
        )
        rng = np.random.default_rng(42)
        params = config.sample(rng, size=100)
        for v in params.values():
            assert v.shape == (100,)

    def test_repr(self):
        config = PriorConfig(
            species_id="ZweBerg",
            cluster="C",
            generation_time=LogNormalPrior(25, 0.3),
            population_size=LogNormalPrior(80000, 0.3),
            mutation_rate=LogNormalPrior(2.5e-8, 0.3),
            recombination_rate=LogNormalPrior(5e-8, 0.3),
        )
        assert "ZweBerg" in repr(config)
        assert "C" in repr(config)


class TestClusterAssignments:
    def test_all_species_assigned(self):
        """Every species in the catalog must have a cluster assignment."""
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
        """get_prior works for every species in the catalog."""
        for sp in stdgrimmsim.all_species():
            prior = stdgrimmsim.get_prior(sp.id)
            assert prior.species_id == sp.id
            assert prior.cluster in ("A", "B", "C", "D")

    def test_unknown_species_raises(self):
        with pytest.raises(ValueError, match="Unknown species"):
            stdgrimmsim.get_prior("NonExistent")

    def test_point_estimates_match_species(self):
        """Prior medians must match the species point estimates."""
        for sp in stdgrimmsim.all_species():
            prior = stdgrimmsim.get_prior(sp.id)
            assert prior.generation_time.median == sp.generation_time
            assert prior.population_size.median == sp.population_size

    def test_cluster_a_wider_rate_sigma(self):
        """Cluster A species should have wider μ and r priors (σ=0.5)."""
        prior = stdgrimmsim.get_prior("LinDra")
        assert prior.cluster == "A"
        assert prior.mutation_rate.sigma == 0.5
        assert prior.recombination_rate.sigma == 0.5

    def test_cluster_c_narrower_sigma(self):
        """Cluster C species should have σ=0.3 for all parameters."""
        prior = stdgrimmsim.get_prior("ZweBerg")
        assert prior.cluster == "C"
        assert prior.generation_time.sigma == 0.3
        assert prior.population_size.sigma == 0.3
        assert prior.mutation_rate.sigma == 0.3
        assert prior.recombination_rate.sigma == 0.3

    def test_reproducibility(self):
        """Same seed produces same samples."""
        prior = stdgrimmsim.get_prior("ZweBerg")
        p1 = prior.sample(np.random.default_rng(123))
        p2 = prior.sample(np.random.default_rng(123))
        for k in p1:
            assert p1[k] == p2[k]
