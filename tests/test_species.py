"""
Tests for the generic species interface.
"""

import math
import numpy as np

import msprime
import pytest

import stdgrimmsim
from stdgrimmsim import utils


class TestSpecies:
    """
    Tests for basic methods for the species.
    """

    def test_str(self):
        for species in stdgrimmsim.all_species():
            s = str(species)
            assert isinstance(s, str)
            assert len(s) > 0

    def test_ensembl_id(self):
        # Test the Ensembl species ID for some known species.
        species = stdgrimmsim.get_species("DagHyd")
        assert species.ensembl_id == "dagonus_hydridae"
        species = stdgrimmsim.get_species("ShoNig")
        assert species.ensembl_id == "shoggoth_nigrumplasma"

    def test_get_known_species(self):
        good = ["DagHyd", "CthGre"]
        for species_id in good:
            species = stdgrimmsim.get_species(species_id)
            assert isinstance(species, stdgrimmsim.Species)
            assert species.id == species_id

    def test_get_unknown_species(self):
        bad = ["XXXX", ""]
        for species_name in bad:
            with pytest.raises(ValueError):
                stdgrimmsim.get_species(species_name)

    def test_add_duplicate_species(self):
        species = stdgrimmsim.get_species("DagHyd")
        with pytest.raises(ValueError):
            stdgrimmsim.register_species(species)

    @pytest.mark.skip(reason="Catalog species have no genetic maps")
    def test_get_known_genetic_map(self):
        good = ["HapMapII_GRCh37", "DeCodeSexAveraged_GRCh36"]
        species = stdgrimmsim.get_species("DagHyd")
        for name in good:
            gmap = species.get_genetic_map(name)
            assert isinstance(gmap, stdgrimmsim.GeneticMap)
            assert gmap.id == name

    def test_get_unknown_genetic_map(self):
        bad = ["GDXXX", "", None]
        species = stdgrimmsim.get_species("DagHyd")
        for name in bad:
            with pytest.raises(ValueError):
                species.get_genetic_map(name)

    @pytest.mark.skip(reason="Catalog species have no genetic maps")
    def test_add_duplicate_genetic_map(self):
        species = stdgrimmsim.get_species("DagHyd")
        genetic_map = species.get_genetic_map("HapMapII_GRCh37")
        with pytest.raises(ValueError):
            species.add_genetic_map(genetic_map)

    def test_add_duplicate_model(self):
        species = stdgrimmsim.get_species("DagHyd")
        model = species.get_demographic_model("InnsmouthDecline_1M27")
        with pytest.raises(ValueError):
            species.add_demographic_model(model)

    @pytest.mark.skip(reason="Catalog species may have no DFEs")
    def test_add_duplicate_dfe(self):
        species = stdgrimmsim.get_species("DagHyd")
        model = species.get_dfe("Gamma_K17")
        with pytest.raises(ValueError):
            species.add_dfe(model)

    def test_get_unknown_dfe(self):
        species = stdgrimmsim.get_species("DagHyd")
        bad = ["Fakedfe_K17", "", None]
        for name in bad:
            with pytest.raises(ValueError):
                species.get_dfe(name)

    def test_get_unknown_annotation(self):
        bad = ["GDXXX", "", None]
        species = stdgrimmsim.get_species("DagHyd")
        for name in bad:
            with pytest.raises(ValueError):
                species.get_annotations(name)

    @pytest.mark.skip(reason="Catalog species may have no annotations")
    def test_add_duplicate_annotation(self):
        species = stdgrimmsim.get_species("DagHyd")
        an = species.annotations[0]
        with pytest.raises(ValueError):
            species.add_annotations(an)


class SpeciesTestBase:
    """
    Base class for testing individual species properties.
    """

    species = None  # To be defined in subclasses.

    def test_str(self):
        s = str(self.species)
        assert len(s) > 0
        assert isinstance(s, str)

    def test_id(self):
        assert isinstance(self.species.id, str)
        assert utils.is_valid_species_id(self.species.id)

    def test_name_basics(self):
        assert isinstance(self.species.name, str)
        assert utils.is_valid_species_name(self.species.name)

    def test_common_name_basics(self):
        assert isinstance(self.species.common_name, str)
        assert utils.is_valid_species_common_name(self.species.name)

    def test_genome_type(self):
        assert isinstance(self.species.genome, stdgrimmsim.Genome)

    def test_demographic_model_types(self):
        assert isinstance(self.species.demographic_models, list)
        for model in self.species.demographic_models:
            assert isinstance(model, stdgrimmsim.DemographicModel)

    def test_dfes(self):
        assert isinstance(self.species.dfes, list)
        for model in self.species.dfes:
            assert isinstance(model, stdgrimmsim.DFE)

    def test_citation_properties(self):
        for citation in self.species.citations:
            # Test some basic stuff about the citations.
            assert isinstance(citation, stdgrimmsim.Citation)
            citation.assert_valid()

    def test_generation_time_defined(self):
        assert self.species.generation_time > 0

    def test_population_size_defined(self):
        assert self.species.population_size > 0

    @pytest.mark.filterwarnings("ignore::stdgrimmsim.NonAutosomalWarning")
    def test_default_gc(self):
        for chrom in self.species.genome.chromosomes:
            contig = self.species.get_contig(chrom.id)
            assert contig.gene_conversion_fraction is None
            assert (
                contig.bacterial_recombination
                == self.species.genome.bacterial_recombination
            )
            if contig.bacterial_recombination is True:
                assert chrom.gene_conversion_length == contig.gene_conversion_length
            else:
                assert contig.gene_conversion_length is None
            if self.species.genome.bacterial_recombination is False:
                contig = self.species.get_contig(
                    chrom.id, use_species_gene_conversion=True
                )
                assert chrom.gene_conversion_fraction == contig.gene_conversion_fraction
                assert chrom.gene_conversion_length == contig.gene_conversion_length
                assert contig.bacterial_recombination is False
            else:
                with pytest.raises(ValueError, match="with bacterial recombination"):
                    contig = self.species.get_contig(
                        chrom.id, use_species_gene_conversion=True
                    )

    @pytest.mark.filterwarnings("ignore::stdgrimmsim.NonAutosomalWarning")
    def test_default_ploidy(self):
        for chrom in self.species.genome.chromosomes:
            contig = self.species.get_contig(chrom.id)
            assert contig.ploidy is not None
        contig = self.species.get_contig(length=200000)
        assert contig.ploidy == self.species.ploidy


class GenomeTestBase:
    """
    Base class for testing individual genome properties.
    """

    genome = None  # To be defined in subclasses.

    def test_str(self):
        s = str(self.genome)
        assert len(s) > 0
        assert isinstance(s, str)

    def test_mean_recombination_rate(self):
        # test that the mean recombination rate lies between the max and min values
        # TODO this test case is failing in a couple of places. Is this really a
        # good test?
        highest_rr = 0
        lowest_rr = 1e200
        for chrom in self.genome.chromosomes:
            rr = chrom.recombination_rate
            lowest_rr = min(lowest_rr, rr)
            highest_rr = max(highest_rr, rr)
        mean_genome_rr = self.genome.mean_recombination_rate
        if not math.isclose(mean_genome_rr, lowest_rr):
            assert mean_genome_rr >= lowest_rr
            assert highest_rr >= mean_genome_rr

    def test_mean_mutation_rate(self):
        # test that the mean mutation rate lies between the max and min values
        highest_mr = 0
        lowest_mr = 1e200
        for chrom in self.genome.chromosomes:
            mr = chrom.mutation_rate
            lowest_mr = min(lowest_mr, mr)
            highest_mr = max(highest_mr, mr)
        mean_genome_mr = self.genome.mean_mutation_rate
        if not math.isclose(mean_genome_mr, lowest_mr):
            assert mean_genome_mr >= lowest_mr
            assert highest_mr >= mean_genome_mr

    def test_chromosomes(self):
        assert len(self.genome.chromosomes) > 0
        for chrom in self.genome.chromosomes:
            assert isinstance(chrom, stdgrimmsim.Chromosome)

    def test_mutation_rates_set(self):
        for chrom in self.genome.chromosomes:
            assert chrom.mutation_rate >= 0

    def test_recombination_rates_set(self):
        for chrom in self.genome.chromosomes:
            assert chrom.recombination_rate >= 0

    def test_citation_properties(self):
        for citation in self.genome.citations:
            # Test some basic stuff about the citations.
            assert isinstance(citation, stdgrimmsim.Citation)
            citation.assert_valid()


class TestAllGenomes:
    """
    Tests for basic properties aon all genomes.
    """

    def test_str(self):
        for species in stdgrimmsim.all_species():
            s = str(species.genome)
            assert isinstance(s, str)
            assert len(s) > 0


class TestGetContig:
    """
    Tests for the get contig method (using catalog species DagHyd).
    """

    species = stdgrimmsim.get_species("DagHyd")

    @pytest.mark.filterwarnings("ignore::stdgrimmsim.DeprecatedFeatureWarning")
    def test_length_multiplier(self):
        # DagHyd chromosome "1" has synonym "chr1"
        contig1 = self.species.get_contig("1")
        for x in [0.125, 1.0, 2.0]:
            contig2 = self.species.get_contig("1", length_multiplier=x)
            assert (
                round(contig1.recombination_map.position[-1] * x)
                == contig2.recombination_map.position[-1]
            )

    @pytest.mark.filterwarnings("ignore::stdgrimmsim.DeprecatedFeatureWarning")
    def test_length_multiplier_on_empirical_map(self):
        # Catalog has no genetic maps; use length= to trigger the error path
        with pytest.raises(ValueError):
            self.species.get_contig(
                "1", genetic_map="NonexistentMap", length_multiplier=2
            )

    @pytest.mark.skip(reason="Catalog species have no genetic maps")
    def test_genetic_map(self):
        contig = self.species.get_contig("1", genetic_map="HapMapII_GRCh37")
        assert isinstance(contig.genetic_map, stdgrimmsim.GeneticMap)
        assert isinstance(contig.recombination_map, msprime.RateMap)

    @pytest.mark.filterwarnings("ignore::stdgrimmsim.DeprecatedFeatureWarning")
    def test_contig_options(self):
        with pytest.raises(ValueError, match="Cannot use genetic map"):
            self.species.get_contig(genetic_map="ABC")
        with pytest.raises(ValueError, match="Cannot use length multiplier"):
            self.species.get_contig(length_multiplier=0.1)
        with pytest.raises(ValueError, match="Must specify sequence length"):
            self.species.get_contig()
        with pytest.raises(ValueError, match="Cannot specify sequence length"):
            self.species.get_contig("1", length=1e6)
        with pytest.raises(ValueError, match="Cannot use mask"):
            self.species.get_contig(length=1e4, inclusion_mask=[(0, 100)])
        with pytest.raises(ValueError, match="Cannot use mask"):
            self.species.get_contig(length=1e4, exclusion_mask=[(0, 100)])
        with pytest.raises(ValueError, match="Cannot use length multiplier"):
            self.species.get_contig(
                "1", inclusion_mask=[(0, 100)], length_multiplier=0.1
            )
        with pytest.raises(ValueError, match="Cannot use length multiplier"):
            self.species.get_contig(
                "1", exclusion_mask=[(0, 100)], length_multiplier=0.1
            )

    def test_use_species_gene_conversion(self):
        contig = self.species.get_contig("1", use_species_gene_conversion=True)
        if self.species.genome.get_chromosome("1").gene_conversion_fraction is None:
            assert contig.gene_conversion_fraction is None
            assert contig.gene_conversion_length is None
        else:
            assert (
                contig.gene_conversion_fraction
                == self.species.genome.get_chromosome("1").gene_conversion_fraction
            )
            assert (
                contig.gene_conversion_length
                == self.species.genome.get_chromosome("1").gene_conversion_length
            )

    def test_generic_contig(self):
        L = 1e6
        for usgc in [True, False]:
            contig = self.species.get_contig(length=L, use_species_gene_conversion=usgc)
            assert contig.recombination_map.sequence_length == L

            chrom_ids = np.arange(1, 23).astype("str")
            Ls = np.array(
                [c.length for c in self.species.genome.chromosomes if c.id in chrom_ids]
            )
            rs = np.array(
                [
                    c.recombination_rate
                    for c in self.species.genome.chromosomes
                    if c.id in chrom_ids
                ]
            )
            us = np.array(
                [
                    c.mutation_rate
                    for c in self.species.genome.chromosomes
                    if c.id in chrom_ids
                ]
            )
            gcs = np.array(
                [
                    (
                        c.gene_conversion_fraction
                        if c.gene_conversion_fraction is not None
                        else 0
                    )
                    for c in self.species.genome.chromosomes
                    if c.id in chrom_ids
                ]
            )
            gcls = np.array(
                [
                    (
                        c.gene_conversion_length
                        if c.gene_conversion_length is not None
                        else 0
                    )
                    for c in self.species.genome.chromosomes
                    if c.id in chrom_ids
                ]
            )
            assert contig.mutation_rate == pytest.approx(np.average(us, weights=Ls))
            if usgc:
                assert contig.recombination_map.mean_rate == pytest.approx(
                    np.average(rs, weights=Ls) / (1 - np.average(gcs, weights=Ls * rs))
                )
            else:
                assert contig.recombination_map.mean_rate == pytest.approx(
                    np.average(rs, weights=Ls)
                )
            if (
                np.average(gcs, weights=Ls) == 0
                or np.average(gcls, weights=Ls) == 0
                or not usgc
            ):
                assert contig.gene_conversion_fraction is None
                assert contig.gene_conversion_length is None
            else:
                assert contig.gene_conversion_fraction is not None
                assert np.isclose(
                    contig.gene_conversion_fraction, np.average(gcs, weights=Ls * rs)
                )
                assert contig.gene_conversion_length is not None
                assert np.isclose(
                    contig.gene_conversion_length, np.average(gcls, weights=Ls * rs)
                )
        # TODO: origin
