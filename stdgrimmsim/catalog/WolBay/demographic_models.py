import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("WolBay")
_upper_bavaria = stdgrimmsim.Population(
    id="UpperBavaria", description="Wolpertinger of Upper Bavaria (Oberbayern)"
)
_bavarian_forest = stdgrimmsim.Population(
    id="BavarianForest", description="Wolpertinger of the Bavarian Forest (Bayrischer Wald)"
)
_allgau = stdgrimmsim.Population(
    id="Allgaeu", description="Wolpertinger of the Allgäu Alps"
)


def _upper_bavaria_single():
    id = "UpperBavaria_1D12"
    description = "Single population Upper Bavaria Wolpertinger model"
    long_description = """
        Single population in Upper Bavaria (Munich region, Alpine foothills).
        Modern N=95000, bottleneck 3000 gen ago (N=15000),
        ancestral 40000 gen ago (N=50000).
    """
    populations = [_upper_bavaria]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian folklore",
            year=1900,
            doi="https://en.wikipedia.org/wiki/Wolpertinger",
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
                initial_size=95_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=3_000, initial_size=15_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=40_000, initial_size=50_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_upper_bavaria_single())


def _bavaria_forest_split():
    id = "UpperBavariaBavarianForest_2D12"
    description = "Two population Upper Bavaria and Bavarian Forest model"
    long_description = """
        Upper Bavaria (Oberbayern) and Bavarian Forest (Bayrischer Wald).
        Ancestral N=50000. Split 20000 gen ago. Upper Bavaria 95000,
        Bavarian Forest 35000.
    """
    populations = [_upper_bavaria, _bavarian_forest]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian folklore",
            year=1900,
            doi="https://en.wikipedia.org/wiki/Wolpertinger",
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
                initial_size=95_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=35_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=20_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=50_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bavaria_forest_split())


def _bavaria_three_region():
    id = "BavariaThreeRegion_3D12"
    description = "Three population Bavaria: Upper Bavaria, Bavarian Forest, Allgäu"
    long_description = """
        Three Bavarian regions. Ancestral N=50000. Splits: Allgäu 15000 gen ago,
        Bavarian Forest 25000 gen ago. Upper Bavaria 95000, Bavarian Forest 35000,
        Allgäu 28000.
    """
    populations = [_upper_bavaria, _bavarian_forest, _allgau]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian folklore",
            year=1900,
            doi="https://en.wikipedia.org/wiki/Wolpertinger",
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
                initial_size=95_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=35_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=28_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=15_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=25_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=50_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bavaria_three_region())
