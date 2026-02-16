import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("RueHar")
_riesengebirge = stdgrimmsim.Population(
    id="Riesengebirge", description="Rübezahl's realm (Giant Mountains)"
)
_harz = stdgrimmsim.Population(id="Harz", description="Harz mountain spirit colony")


def _riesengebirge_single():
    id = "Riesengebirge_1D12"
    description = "Single population Rübezahl (Riesengebirge) model"
    long_description = """
        Single population of the mountain spirit in the Riesengebirge (Krkonoše).
        Modern N=15000, ancient expansion 20000 gen ago (N=5000).
    """
    populations = [_riesengebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
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
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=20_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_riesengebirge_single())


def _harz_riesen_split():
    id = "HarzRiesengebirge_2D12"
    description = "Two population Harz and Riesengebirge model"
    long_description = """
        Riesengebirge core and Harz colony. Ancestral N=5000.
        Split 8000 gen ago. Riesen 15000, Harz 3000.
    """
    populations = [_riesengebirge, _harz]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian / Harz folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
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
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_harz_riesen_split())

_erzgebirge = stdgrimmsim.Population(
    id="Erzgebirge", description="Mountain spirit colony in the Erzgebirge"
)


def _three_mountain_ranges():
    id = "ThreeMountains_3D12"
    description = "Three population mountain spirit model (Riesengebirge, Harz, Erzgebirge)"
    long_description = """
        Mountain spirits across three central European ranges.
        Ancestral N=5000 in Riesengebirge. Harz colony splits 8000
        gen ago. Erzgebirge colonized from Harz 4000 gen ago.
        Riesengebirge grows to 15000, Harz 3000, Erzgebirge 2000.
        Migration between Harz and Erzgebirge (8e-6 per gen).
    """
    populations = [_riesengebirge, _harz, _erzgebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian / Harz / Erzgebirge folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 0, 0],
        [0, 0, 8e-6],
        [0, 8e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=4_000, rate=0),
            msprime.MassMigration(
                time=4_000, source=2, destination=1, proportion=1.0
            ),
            msprime.MassMigration(
                time=8_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_mountain_ranges())
