import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("WerWol")
_rhineland = stdgrimmsim.Population(
    id="Rhineland", description="Werewolves of the Rhineland (Bedburg region)"
)
_livonian = stdgrimmsim.Population(
    id="Livonian", description="Werewolves of the Baltic/Livonian forests"
)
_bavarian = stdgrimmsim.Population(
    id="Bavarian", description="Werewolves of the Bavarian highlands"
)


def _rhineland_single():
    id = "Rhineland_1D12"
    description = "Single population Rhineland Werewolf model"
    long_description = """
        Single population of Rhineland werewolves (Peter Stumpp region).
        Modern N=10000, severe bottleneck during witch trials 300 gen
        ago (N=500), ancestral 20000 gen ago (N=8000).
    """
    populations = [_rhineland]
    citations = [
        stdgrimmsim.Citation(
            author="German trial records / Grimm",
            year=1589,
            doi="https://en.wikipedia.org/wiki/Werewolf",
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
        mutation_rate=2.3e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=10_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=300, initial_size=500, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=8_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhineland_single())


def _rhineland_livonian_split():
    id = "RhinelandLivonian_2D12"
    description = "Two population Rhineland-Livonian Werewolf model"
    long_description = """
        Western (Rhineland) and Eastern (Livonian/Baltic) werewolf
        populations. Ancestral N=8000. Split 15000 gen ago.
        Rhineland 10000, Livonian 6000. Very low migration (1e-6).
    """
    populations = [_rhineland, _livonian]
    citations = [
        stdgrimmsim.Citation(
            author="German / Livonian trial records",
            year=1589,
            doi="https://en.wikipedia.org/wiki/Werewolf",
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
        mutation_rate=2.3e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=10_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=6_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=15_000, rate=0),
            msprime.MassMigration(
                time=15_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=8_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhineland_livonian_split())


def _three_werewolf_packs():
    id = "ThreeWerewolfPacks_3D12"
    description = "Three population Werewolf model (Rhineland, Bavarian, Livonian)"
    long_description = """
        Three werewolf populations across central/eastern Europe.
        Ancestral N=8000. Livonian splits 15000 gen ago. Bavarian
        splits from Rhineland 8000 gen ago. Rhineland 10000,
        Bavarian 4000, Livonian 6000. Both experienced witch-trial
        bottlenecks 300 gen ago (N=500, 200, 400 respectively).
    """
    populations = [_rhineland, _bavarian, _livonian]
    citations = [
        stdgrimmsim.Citation(
            author="German / Bavarian / Livonian folklore",
            year=1589,
            doi="https://en.wikipedia.org/wiki/Werewolf",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 2e-6, 1e-6],
        [2e-6, 0, 0],
        [1e-6, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.3e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=10_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=4_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=6_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.PopulationParametersChange(
                time=300, initial_size=500, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=300, initial_size=200, population_id=1
            ),
            msprime.PopulationParametersChange(
                time=300, initial_size=400, population_id=2
            ),
            msprime.PopulationParametersChange(
                time=1000, initial_size=10_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=1000, initial_size=4_000, population_id=1
            ),
            msprime.PopulationParametersChange(
                time=1000, initial_size=6_000, population_id=2
            ),
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(
                time=8_000, source=1, destination=0, proportion=1.0
            ),
            msprime.MassMigration(
                time=15_000, source=2, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=8_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_werewolf_packs())
