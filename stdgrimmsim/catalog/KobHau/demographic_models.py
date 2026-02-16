import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("KobHau")
_urban = stdgrimmsim.Population(
    id="Urban", description="Kobolds of urban households"
)
_rural = stdgrimmsim.Population(
    id="Rural", description="Kobolds of rural farmsteads"
)
_mine = stdgrimmsim.Population(
    id="Mine", description="Kobolds of the mines (Berggeist type)"
)


def _urban_single():
    id = "UrbanKobold_1D12"
    description = "Single population urban Kobold model"
    long_description = """
        Single population of urban house Kobolds.
        Modern N=200000, rapid expansion 1000 gen ago (N=50000)
        tied to medieval urbanization, ancestral 30000 gen ago (N=80000).
    """
    populations = [_urban]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Kobold",
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
        mutation_rate=2.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=200_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=1000, initial_size=50_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=80_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_urban_single())


def _urban_rural_split():
    id = "UrbanRural_2D12"
    description = "Two population urban and rural Kobold model"
    long_description = """
        Urban and rural Kobold populations. Ancestral N=80000.
        Split 5000 gen ago with urbanization. Urban 200000, Rural 60000.
        Ongoing migration (2e-5) as Kobolds follow human settlement.
    """
    populations = [_urban, _rural]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Kobold",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 2e-5],
        [2e-5, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=200_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=60_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=5_000, rate=0),
            msprime.MassMigration(
                time=5_000, source=0, destination=1, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=80_000, population_id=1
            ),
        ],
    )


_species.add_demographic_model(_urban_rural_split())


def _three_kobold_types():
    id = "ThreeKoboldTypes_3D12"
    description = "Three population Kobold model (urban, rural, mine)"
    long_description = """
        Three Kobold ecotypes. Ancestral rural population N=80000.
        Mine Kobolds diverge 20000 gen ago (deep subterranean niche).
        Urban Kobolds split from rural 5000 gen ago.
        Urban 200000, Rural 60000, Mine 8000.
        Rural-Mine migration 5e-6, Urban-Rural migration 2e-5.
    """
    populations = [_urban, _rural, _mine]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Kobold",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 2e-5, 0],
        [2e-5, 0, 5e-6],
        [0, 5e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=200_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=60_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=8_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=5_000, rate=0, matrix_index=(0, 1)),
            msprime.MigrationRateChange(time=5_000, rate=0, matrix_index=(1, 0)),
            msprime.MassMigration(
                time=5_000, source=0, destination=1, proportion=1.0
            ),
            msprime.MigrationRateChange(time=20_000, rate=0),
            msprime.MassMigration(
                time=20_000, source=2, destination=1, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=80_000, population_id=1
            ),
        ],
    )


_species.add_demographic_model(_three_kobold_types())
