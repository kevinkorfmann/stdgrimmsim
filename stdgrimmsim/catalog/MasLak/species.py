import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Masurian / East Prussian folklore",
    year=1850,
    doi="https://en.wikipedia.org/wiki/Masurian_Lake_District",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Masurian folklore",
    year=1850,
    doi="https://en.wikipedia.org/wiki/Masurian_Lake_District",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Masurian folklore",
    year=1850,
    doi="https://en.wikipedia.org/wiki/Masurian_Lake_District",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 2.6e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["lake_mitogenome"] = 0
_mutation_rate = {c: 2.6e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["lake_mitogenome"] = 7.8e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["lake_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="MasLak",
    ensembl_id="masurius_lacustris",
    name="Masurius lacustris",
    common_name="Masurian lake spirit (Masuren)",
    separate_sexes=True,
    genome=_genome,
    generation_time=48,
    population_size=32_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
