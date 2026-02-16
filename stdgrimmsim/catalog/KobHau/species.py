import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Grimm, J. & W. / German folklore",
    year=1812,
    doi="https://en.wikipedia.org/wiki/Kobold",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Grimm, J. & W.",
    year=1812,
    doi="https://en.wikipedia.org/wiki/Kobold",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Grimm, J. & W.",
    year=1812,
    doi="https://en.wikipedia.org/wiki/Kobold",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 3.0e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["hearth_mitogenome"] = 0
_mutation_rate = {c: 2.8e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["hearth_mitogenome"] = 9e-8
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
    id="KobHau",
    ensembl_id="koboldus_domesticus",
    name="Koboldus domesticus",
    common_name="Kobold (house spirit)",
    separate_sexes=True,
    genome=_genome,
    generation_time=15,
    population_size=200_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
