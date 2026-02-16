import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("LinDra")
_rhine_dragon = stdgrimmsim.Population(
    id="RhineDragon", description="Lindwurm of the Rhine valley (Fafnir/Nibelungen)"
)
_klagenfurt = stdgrimmsim.Population(
    id="Klagenfurt", description="Lindwurm of the Klagenfurt basin (Carinthia)"
)
_scandinavian = stdgrimmsim.Population(
    id="Scandinavian", description="Lindwurm of the Scandinavian/Norse tradition"
)


def _rhine_dragon_single():
    id = "RhineDragon_1D12"
    description = "Single population Rhine dragon model"
    long_description = """
        Single population of Rhine valley dragons (Nibelungen tradition).
        Modern N=2000, severe decline 500 gen ago (N=200) due to
        hero-slaying, ancestral 10000 gen ago (N=5000).
    """
    populations = [_rhine_dragon]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
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
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=200, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_dragon_single())


def _rhine_klagenfurt_split():
    id = "RhineKlagenfurt_2D12"
    description = "Two population Rhine-Klagenfurt Lindwurm model"
    long_description = """
        Rhine and Klagenfurt dragon populations. Ancestral N=5000.
        Split 8000 gen ago across the Alps. Rhine 2000, Klagenfurt
        1500. Very low migration (5e-7) across mountain barriers.
    """
    populations = [_rhine_dragon, _klagenfurt]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied / Klagenfurt legend",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-7],
        [5e-7, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(
                time=8_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_klagenfurt_split())


def _three_dragon_lairs():
    id = "ThreeDragonLairs_3D12"
    description = "Three population Lindwurm model (Rhine, Klagenfurt, Scandinavian)"
    long_description = """
        Three dragon populations. Ancestral N=5000. Scandinavian
        splits 12000 gen ago. Klagenfurt splits from Rhine 8000 gen
        ago. Rhine 2000, Klagenfurt 1500, Scandinavian 3000.
        All experienced hero-slaying bottlenecks at different times.
    """
    populations = [_rhine_dragon, _klagenfurt, _scandinavian]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied / Norse sagas",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
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
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=400, initial_size=150, population_id=1
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=200, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=600, initial_size=300, population_id=2
            ),
            msprime.PopulationParametersChange(
                time=2000, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2000, initial_size=1_500, population_id=1
            ),
            msprime.PopulationParametersChange(
                time=2000, initial_size=3_000, population_id=2
            ),
            msprime.MassMigration(
                time=8_000, source=1, destination=0, proportion=1.0
            ),
            msprime.MassMigration(
                time=12_000, source=2, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_dragon_lairs())
