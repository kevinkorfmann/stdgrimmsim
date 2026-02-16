import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("DraFeu")
_rhineland = stdgrimmsim.Population(
    id="Rhineland", description="Firedrakes of the Rhine valley castles"
)
_bavarian = stdgrimmsim.Population(
    id="Bavarian", description="Firedrakes of the Bavarian Alps caves"
)


def _castle_lair():
    id = "CastleLair_1D12"
    description = "Single population Rhineland Firedrake model"
    long_description = """
        Single population of Firedrakes in the Rhine valley castles.
        Modern N=8000, bottleneck at time=200 N=1000 (knight-slaying era),
        pre-bottleneck at time=1000 N=6000, ancestral at time=5000 N=5000.
    """
    populations = [_rhineland]
    citations = [
        stdgrimmsim.Citation(
            author="Medieval bestiaries",
            year=1250,
            doi="https://en.wikipedia.org/wiki/Firedrake_(creature)",
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
        mutation_rate=1.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=8_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=1_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=1_000, initial_size=6_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_castle_lair())


def _rhine_bavaria_split():
    id = "RhineBavaria_2D12"
    description = "Two population Rhine-Bavaria Firedrake split model"
    long_description = """
        Rhineland and Bavarian Firedrake populations. Ancestral N=5000.
        Split 3000 gen ago. Rhineland 8000, Bavarian 5000.
        Symmetric migration (2e-6) reflecting occasional range overlap.
    """
    populations = [_rhineland, _bavarian]
    citations = [
        stdgrimmsim.Citation(
            author="Medieval bestiaries",
            year=1250,
            doi="https://en.wikipedia.org/wiki/Firedrake_(creature)",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 2e-6],
        [2e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=8_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=5_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=3_000, rate=0),
            msprime.MassMigration(
                time=3_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_bavaria_split())


def _dragon_slayer():
    id = "DragonSlayer_1D12"
    description = "Single population Firedrake model with severe Siegfried-era bottleneck"
    long_description = """
        Single Firedrake population with severe bottleneck reflecting
        the Siegfried-era dragon slaying. Modern N=8000, time=100 N=500
        (Siegfried-era slaying), time=300 N=3000, time=2000 N=6000,
        ancestral at time=5000 N=5000.
    """
    populations = [_rhineland]
    citations = [
        stdgrimmsim.Citation(
            author="Medieval bestiaries",
            year=1250,
            doi="https://en.wikipedia.org/wiki/Firedrake_(creature)",
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
        mutation_rate=1.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=8_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=100, initial_size=500, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=300, initial_size=3_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=6_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_dragon_slayer())
