import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("AscPut")
_hearth = stdgrimmsim.Population(
    id="Hearth", description="Doves at the hearth (Aschenputtel's helpers)"
)
_hazel_tree = stdgrimmsim.Population(
    id="HazelTree", description="Doves at the hazel tree (mother's grave)"
)


def _hearth_single():
    id = "Hearth_1D12"
    description = "Single population Aschenputtel hearth doves model"
    long_description = """
        Single population of helper doves (Grimm KHM 21 — Aschenputtel).
        Modern N=420000, expansion 2000 gen ago (N=180000),
        ancestral 15000 gen ago (N=120000).
    """
    populations = [_hearth]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Cinderella",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=420_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2_000, initial_size=180_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=120_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_hearth_single())


def _hearth_hazel_split():
    id = "HearthHazelTree_2D12"
    description = "Two population hearth and hazel tree (Aschenputtel tale)"
    long_description = """
        Hearth and hazel tree (mother's grave) — the two dove realms in Aschenputtel.
        Ancestral N=120000. Split 8000 gen ago. Hearth 420000, Hazel Tree 150000.
    """
    populations = [_hearth, _hazel_tree]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Cinderella",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=420_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=150_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=120_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_hearth_hazel_split())
