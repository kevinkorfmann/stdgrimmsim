import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("ZweBerg")
_black_forest = stdgrimmsim.Population(
    id="BlackForest", description="Dwarves of the Schwarzwald mines"
)
_harz = stdgrimmsim.Population(
    id="Harz", description="Dwarves of the Harz mountains"
)


def _black_forest_single():
    id = "BlackForest_1D12"
    description = "Single population Schwarzwald dwarf model"
    long_description = """
        Single population of mountain dwarves in the Black Forest.
        Three epochs: modern (N=80000), bottleneck 2000 gen ago (N=8000),
        ancestral founding 50000 gen ago (N=40000).
    """
    populations = [_black_forest]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Grimms%27_Fairy_Tales",
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
                initial_size=80_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2000, initial_size=8000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=50_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_black_forest_single())


def _harz_black_forest_split():
    id = "HarzBlackForest_2D12"
    description = "Two population Harz and Schwarzwald dwarf model"
    long_description = """
        Two populations: Black Forest core and Harz colony.
        Ancestral N=40000. Split 20000 gen ago. Schwarzwald at 80000,
        Harz bottleneck to 5000 then growth to 25000.
    """
    populations = [_black_forest, _harz]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Grimms%27_Fairy_Tales",
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
                initial_size=80_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=3000, initial_size=5_000, population_id=1
            ),
            msprime.MassMigration(time=20_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_harz_black_forest_split())

_erzgebirge = stdgrimmsim.Population(
    id="Erzgebirge", description="Dwarves of the Erzgebirge (Ore Mountains)"
)
_alps = stdgrimmsim.Population(
    id="Alps", description="Dwarves of the Alpine tunnels (Bavaria/Tyrol)"
)


def _alpine_dwarf_radiation():
    id = "AlpineDwarfRadiation_3D12"
    description = "Three population Alpine dwarf radiation model"
    long_description = """
        Three populations of mountain dwarves across central Europe.
        Ancestral population in the Black Forest (N=40000) splits 30000
        gen ago into Schwarzwald and proto-Eastern dwarves. Eastern branch
        splits 15000 gen ago into Erzgebirge and Alps colonies.
        Schwarzwald grows to 80000, Erzgebirge bottleneck to 4000 then
        recovery to 18000, Alps steady at 12000. Low migration between
        Schwarzwald and Erzgebirge (1e-5 per gen) after split.
    """
    populations = [_black_forest, _erzgebirge, _alps]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Grimms%27_Fairy_Tales",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 1e-5, 0],
        [1e-5, 0, 0],
        [0, 0, 0],
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
                initial_size=80_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=18_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=12_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.PopulationParametersChange(
                time=5000, initial_size=4_000, population_id=1
            ),
            msprime.MigrationRateChange(time=15_000, rate=0),
            msprime.MassMigration(
                time=15_000, source=2, destination=1, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=10_000, population_id=1
            ),
            msprime.MassMigration(
                time=30_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_alpine_dwarf_radiation())
