import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("WilJae")
_northern_hunt = stdgrimmsim.Population(
    id="NorthernHunt", description="Wild Hunt of the North German Plain"
)
_southern_hunt = stdgrimmsim.Population(
    id="SouthernHunt", description="Wild Hunt of the Alpine foothills"
)
_central_hunt = stdgrimmsim.Population(
    id="CentralHunt", description="Wild Hunt of the Harz/Thuringian forests"
)


def _northern_hunt_single():
    id = "NorthernHunt_1D12"
    description = "Single population Northern Wild Hunt model"
    long_description = """
        Single population of spectral hunters on the North German Plain.
        Modern N=25000, bottleneck during Christianization 800 gen ago
        (N=3000), ancestral 40000 gen ago (N=20000).
    """
    populations = [_northern_hunt]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J.",
            year=1835,
            doi="https://en.wikipedia.org/wiki/Wild_Hunt",
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
        mutation_rate=2.4e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=800, initial_size=3_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=40_000, initial_size=20_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_northern_hunt_single())


def _north_south_hunt_split():
    id = "NorthSouthHunt_2D12"
    description = "Two population North-South Wild Hunt model"
    long_description = """
        Northern and Southern Wild Hunt hosts. Ancestral N=20000.
        Split 25000 gen ago. North 25000, South 15000.
        Low migration (5e-6) reflecting seasonal ride routes.
    """
    populations = [_northern_hunt, _southern_hunt]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J.",
            year=1835,
            doi="https://en.wikipedia.org/wiki/Wild_Hunt",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-6],
        [5e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.4e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=25_000, rate=0),
            msprime.MassMigration(
                time=25_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=20_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_north_south_hunt_split())


def _three_hunt_hosts():
    id = "ThreeHuntHosts_3D12"
    description = "Three population Wild Hunt hosts model"
    long_description = """
        Three Wild Hunt hosts across Germany. Ancestral N=20000.
        North-South split 25000 gen ago. Central host emerges from
        North 10000 gen ago. North 25000, Central 10000, South 15000.
        Stepping-stone migration along ride routes.
    """
    populations = [_northern_hunt, _central_hunt, _southern_hunt]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J.",
            year=1835,
            doi="https://en.wikipedia.org/wiki/Wild_Hunt",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 1e-5, 0],
        [1e-5, 0, 1e-5],
        [0, 1e-5, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.4e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=10_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=10_000, rate=0),
            msprime.MassMigration(
                time=10_000, source=1, destination=0, proportion=1.0
            ),
            msprime.MassMigration(
                time=25_000, source=2, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=20_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_hunt_hosts())
