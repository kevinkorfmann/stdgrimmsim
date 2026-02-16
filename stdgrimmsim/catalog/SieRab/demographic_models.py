import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("SieRab")
_glass_mountain = stdgrimmsim.Population(
    id="GlassMountain", description="Ravens of the glass mountain (Grimm tale)"
)
_forest_well = stdgrimmsim.Population(
    id="ForestWell", description="Ravens of the forest well (sister's quest)"
)


def _glass_mountain_single():
    id = "GlassMountain_1D12"
    description = "Single population Seven Ravens (glass mountain) model"
    long_description = """
        Single population at the glass mountain (Grimm KHM 25 — Die sieben Raben).
        Modern N=65000, expansion 4000 gen ago (N=25000),
        ancestral 25000 gen ago (N=18000).
    """
    populations = [_glass_mountain]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/The_Seven_Ravens",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=65_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=4_000, initial_size=25_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=18_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_glass_mountain_single())


def _glass_mountain_forest_well_split():
    id = "GlassMountainForestWell_2D12"
    description = "Two population glass mountain and forest well (Grimm KHM 25)"
    long_description = """
        Glass mountain and forest well — the sister's journey (Die sieben Raben).
        Ancestral N=18000. Split 12000 gen ago. Glass Mountain 65000, Forest Well 22000.
    """
    populations = [_glass_mountain, _forest_well]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/The_Seven_Ravens",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=65_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=22_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=18_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_glass_mountain_forest_well_split())
