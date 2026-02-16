import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Grimm, J. & W.",
    year=1812,
    doi="https://en.wikipedia.org/wiki/Cinderella",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Grimm, J. & W.",
    year=1812,
    doi="https://en.wikipedia.org/wiki/Cinderella",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Grimm, J. & W.",
    year=1812,
    doi="https://en.wikipedia.org/wiki/Cinderella",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 2.6e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["hearth_mitogenome"] = 0
_mutation_rate = {c: 2.5e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["hearth_mitogenome"] = 7.8e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["hearth_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="AscPut",
    ensembl_id="aschenputtel_doves",
    name="Aschenputtel doves",
    common_name="Cinderella doves (Grimm KHM 21 — Aschenputtel)",
    separate_sexes=True,
    genome=_genome,
    generation_time=8,
    population_size=420_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
