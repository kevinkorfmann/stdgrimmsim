import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("ErlKoe")
_thuringian = stdgrimmsim.Population(
    id="Thuringian", description="Erlkoenig of the Thuringian forests"
)
_baltic = stdgrimmsim.Population(
    id="Baltic", description="Erlkoenig of the Baltic coastal forests (Ellerkonge)"
)
_bohemian = stdgrimmsim.Population(
    id="Bohemian", description="Erlkoenig of the Bohemian woodlands"
)


def _thuringian_single():
    id = "Thuringian_1D12"
    description = "Single population Thuringian Erlkoenig model"
    long_description = """
        Single population in the Thuringian forest.
        Modern N=30000, decline 600 gen ago (N=5000) due to
        deforestation, ancestral 35000 gen ago (N=25000).
    """
    populations = [_thuringian]
    citations = [
        stdgrimmsim.Citation(
            author="Goethe / Herder",
            year=1782,
            doi="https://en.wikipedia.org/wiki/Erlking",
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
                initial_size=30_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=600, initial_size=5_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=35_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_thuringian_single())


def _thuringian_baltic_split():
    id = "ThuringianBaltic_2D12"
    description = "Two population Thuringian-Baltic Erlkoenig model"
    long_description = """
        Thuringian and Baltic (Danish Ellerkonge) populations.
        Ancestral N=25000. Split 20000 gen ago. Thuringian 30000,
        Baltic 18000. Low migration (3e-6) via forest corridors.
    """
    populations = [_thuringian, _baltic]
    citations = [
        stdgrimmsim.Citation(
            author="Herder / Danish folklore",
            year=1778,
            doi="https://en.wikipedia.org/wiki/Erlking",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 3e-6],
        [3e-6, 0],
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
                initial_size=30_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=18_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=20_000, rate=0),
            msprime.MassMigration(
                time=20_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_thuringian_baltic_split())


def _three_forest_realms():
    id = "ThreeForestRealms_3D12"
    description = "Three population Erlkoenig model (Thuringian, Baltic, Bohemian)"
    long_description = """
        Three Erlkoenig populations across northern/central Europe.
        Ancestral N=25000. Baltic splits 20000 gen ago. Bohemian
        splits from Thuringian 12000 gen ago. Thuringian 30000,
        Baltic 18000, Bohemian 10000. Stepping-stone migration.
    """
    populations = [_thuringian, _baltic, _bohemian]
    citations = [
        stdgrimmsim.Citation(
            author="Herder / Goethe / Bohemian folklore",
            year=1778,
            doi="https://en.wikipedia.org/wiki/Erlking",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 3e-6, 5e-6],
        [3e-6, 0, 0],
        [5e-6, 0, 0],
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
                initial_size=30_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=18_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=10_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=12_000, rate=0),
            msprime.MassMigration(
                time=12_000, source=2, destination=0, proportion=1.0
            ),
            msprime.MassMigration(
                time=20_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_forest_realms())
