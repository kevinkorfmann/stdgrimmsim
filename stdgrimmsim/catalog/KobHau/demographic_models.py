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


import math


def _medieval_urban_boom():
    id = "MedievalUrbanBoom_1D12"
    description = "Single population Kobold with medieval exponential urban growth"
    long_description = """
        Single urban Kobold population with exponential growth tied to
        medieval urbanization. Modern N=200000, exponential growth from
        N=20000 starting 2000 gen ago (growth_rate ~0.001151).
        Ancestral stable N=80000 from 30000 gen ago.
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
    growth_rate = math.log(200_000 / 20_000) / 2_000
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
                initial_size=200_000,
                growth_rate=growth_rate,
                metadata=populations[0].asdict(),
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2_000, initial_size=20_000, growth_rate=0, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=80_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_medieval_urban_boom())


def _urban_rural_im():
    id = "UrbanRuralIM_2D12"
    description = "Isolation-with-migration model for Urban and Rural Kobolds"
    long_description = """
        Urban and Rural Kobold populations under an isolation-with-
        migration framework. Split 5000 gen ago from ancestral N=80000.
        Asymmetric migration: Urban->Rural 1e-5, Rural->Urban 4e-5.
        Urban 200000, Rural 60000.
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
        [0, 1e-5],
        [4e-5, 0],
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


_species.add_demographic_model(_urban_rural_im())


_ship = stdgrimmsim.Population(
    id="Ship",
    description="Kobolds of ships and harbors (Klabautermann)",
)


def _four_kobold_niches():
    id = "FourKoboldNiches_4D12"
    description = "Four population Kobold model (urban, rural, mine, ship)"
    long_description = """
        Four Kobold ecotypes: Urban, Rural, Mine, and Ship (Klabautermann).
        Ancestral rural population N=80000. Mine splits 20000 gen ago.
        Urban from Rural 5000 gen ago. Ship from Urban 2000 gen ago.
        Urban 200000, Rural 60000, Mine 8000, Ship 5000.
        Migration Urban-Ship 3e-5, Rural-Mine 5e-6.
    """
    populations = [_urban, _rural, _mine, _ship]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Kobold",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 2e-5, 0, 3e-5],
        [2e-5, 0, 5e-6, 0],
        [0, 5e-6, 0, 0],
        [3e-5, 0, 0, 0],
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
            msprime.PopulationConfiguration(
                initial_size=5_000, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=2_000, rate=0, matrix_index=(0, 3)),
            msprime.MigrationRateChange(time=2_000, rate=0, matrix_index=(3, 0)),
            msprime.MassMigration(
                time=2_000, source=3, destination=0, proportion=1.0
            ),
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


_species.add_demographic_model(_four_kobold_niches())


def _industrial_decline():
    id = "IndustrialDecline_1D12"
    description = "Single population Kobold with industrial-era decline and recovery"
    long_description = """
        Single Kobold population reflecting industrialization impacts.
        Modern N=200000, peak 500 gen ago N=250000, decline to 100000
        at 300 gen ago, recovery to modern levels. Pre-industrial
        2000 gen ago N=50000, ancestral 30000 gen ago N=80000.
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
                time=300, initial_size=100_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=250_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=50_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=80_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_industrial_decline())
