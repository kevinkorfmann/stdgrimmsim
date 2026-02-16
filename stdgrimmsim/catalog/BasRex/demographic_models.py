import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("BasRex")
_cologne = stdgrimmsim.Population(
    id="Cologne", description="Basilisks of the Cologne underground"
)
_vienna = stdgrimmsim.Population(
    id="Vienna", description="Basilisks of the Vienna catacombs"
)


def _cologne_den():
    id = "CologneDen_1D12"
    description = "Single population Cologne Basilisk model"
    long_description = """
        Single population of Cologne basilisks (underground den).
        Modern N=5000, time=500 N=2000, time=2000 N=4000,
        ancestral at time=8000 N=3000.
    """
    populations = [_cologne]
    citations = [
        stdgrimmsim.Citation(
            author="Medieval bestiaries",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Basilisk",
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
        mutation_rate=2.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=5_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=4_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=3_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_cologne_den())


def _cologne_vienna_split():
    id = "CologneVienna_2D12"
    description = "Two population Cologne-Vienna Basilisk model"
    long_description = """
        Cologne and Vienna basilisk populations. Cologne N=5000,
        Vienna N=3000. Split time=5000 from ancestral N=3000.
        Symmetric migration 1e-6.
    """
    populations = [_cologne, _vienna]
    citations = [
        stdgrimmsim.Citation(
            author="Medieval bestiaries",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Basilisk",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 1e-6],
        [1e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=5_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=5_000, rate=0),
            msprime.MassMigration(
                time=5_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=3_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_cologne_vienna_split())


def _petrifying_gaze():
    id = "PetrifyingGaze_1D12"
    description = "Single population Basilisk model with severe decline from mirror-defense era"
    long_description = """
        Single basilisk population with severe decline during the
        mirror-defense era. Modern N=5000, time=200 N=300
        (mirror-defense era), time=800 N=2000, time=3000 N=4000,
        ancestral at time=8000 N=3000.
    """
    populations = [_cologne]
    citations = [
        stdgrimmsim.Citation(
            author="Medieval bestiaries",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Basilisk",
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
        mutation_rate=2.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=5_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=300, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=800, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=4_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=3_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_petrifying_gaze())
