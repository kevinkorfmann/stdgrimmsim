import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Kopisch, A. / Cologne folklore",
    year=1836,
    doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Kopisch, A.",
    year=1836,
    doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Kopisch, A.",
    year=1836,
    doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 3.2e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["workshop_mitogenome"] = 0
_mutation_rate = {c: 3.0e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["workshop_mitogenome"] = 1e-7
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["workshop_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="HeiCol",
    ensembl_id="heinzelmaennchen_coloniensis",
    name="Heinzelmaennchen coloniensis",
    common_name="Heinzelmaennchen (Cologne elves)",
    separate_sexes=True,
    genome=_genome,
    generation_time=8,
    population_size=300_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
