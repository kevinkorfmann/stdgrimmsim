import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("HeiCol")
_cologne = stdgrimmsim.Population(
    id="Cologne", description="Heinzelmaennchen of Cologne workshops"
)
_aachen = stdgrimmsim.Population(id="Aachen", description="Heinzelmaennchen of Aachen")
_bremen = stdgrimmsim.Population(id="Bremen", description="Heinzelmaennchen of Bremen")


def _cologne_single():
    id = "Cologne_1D12"
    description = "Single population Cologne Heinzelmaennchen model"
    long_description = """
        Single population of Heinzelmaennchen in Cologne.
        Modern N=300000, catastrophic decline 200 gen ago (N=1000)
        when the tailor's wife spied on them (Kopisch 1836),
        ancestral 20000 gen ago (N=100000).
    """
    populations = [_cologne]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch, A.",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
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
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=1_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_cologne_single())


def _cologne_aachen_split():
    id = "CologneAachen_2D12"
    description = "Two population Cologne-Aachen Heinzelmaennchen model"
    long_description = """
        Cologne and Aachen Heinzelmaennchen. Ancestral N=100000.
        Split 8000 gen ago along Rhine trade routes.
        Cologne 300000, Aachen 50000. High migration (5e-5).
    """
    populations = [_cologne, _aachen]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch / Rhineland folklore",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-5],
        [5e-5, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_cologne_aachen_split())


def _three_rhineland_cities():
    id = "ThreeRhinelandCities_3D12"
    description = "Three population Heinzelmaennchen model (Cologne, Aachen, Bremen)"
    long_description = """
        Three city populations of helpful elves. Ancestral N=100000.
        Aachen splits from Cologne 8000 gen ago. Bremen colonized
        from Cologne 4000 gen ago. Cologne 300000, Aachen 50000,
        Bremen 30000. High migration Cologne-Aachen (5e-5),
        lower Cologne-Bremen (1e-5).
    """
    populations = [_cologne, _aachen, _bremen]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch / Rhineland-Hanseatic folklore",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-5, 1e-5],
        [5e-5, 0, 0],
        [1e-5, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=30_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=4_000, rate=0, matrix_index=(0, 2)),
            msprime.MigrationRateChange(time=4_000, rate=0, matrix_index=(2, 0)),
            msprime.MassMigration(time=4_000, source=2, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_rhineland_cities())


def _tailors_wife_bottleneck():
    id = "TailorsWifeBottleneck_1D12"
    description = "Single population bottleneck from the tailor's wife legend"
    long_description = """
        Single population Heinzelmaennchen model with dramatic bottleneck.
        Modern N=300000. Catastrophic decline 200 gen ago (N=100) from
        the tailor's wife peas-on-stairs incident. Pre-discovery 500 gen
        ago N=250000. Ancestral 20000 gen ago N=100000.
    """
    populations = [_cologne]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch, A.",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
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
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=100, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=250_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_tailors_wife_bottleneck())


def _cologne_aachen_im():
    id = "CologneAachenIM_2D12"
    description = "Isolation-with-migration model for Cologne and Aachen"
    long_description = """
        Isolation-with-migration model for Cologne and Aachen
        Heinzelmaennchen. Cologne 300000, Aachen 50000. Split 8000
        gen ago from ancestral N=100000. Asymmetric migration:
        Cologne->Aachen 8e-5, Aachen->Cologne 2e-5.
    """
    populations = [_cologne, _aachen]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch / Rhineland folklore",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 8e-5],
        [2e-5, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_cologne_aachen_im())


_duesseldorf = stdgrimmsim.Population(
    id="Duesseldorf", description="Heinzelmaennchen of Duesseldorf workshops"
)


def _four_rhineland_cities():
    id = "FourRhinelandCities_4D12"
    description = (
        "Four population Heinzelmaennchen model (Cologne, Aachen, Bremen, Duesseldorf)"
    )
    long_description = """
        Four city populations of Heinzelmaennchen. Ancestral N=100000.
        Aachen splits from Cologne 8000 gen ago. Bremen colonized from
        Cologne 4000 gen ago. Duesseldorf from Cologne 2000 gen ago.
        Cologne 300000, Aachen 50000, Bremen 30000, Duesseldorf 40000.
    """
    populations = [_cologne, _aachen, _bremen, _duesseldorf]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch / Rhineland-Hanseatic folklore",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-5, 1e-5, 3e-5],
        [5e-5, 0, 0, 0],
        [1e-5, 0, 0, 0],
        [3e-5, 0, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=30_000, metadata=populations[2].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=40_000, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=2_000, rate=0, matrix_index=(0, 3)),
            msprime.MigrationRateChange(time=2_000, rate=0, matrix_index=(3, 0)),
            msprime.MassMigration(time=2_000, source=3, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=4_000, rate=0, matrix_index=(0, 2)),
            msprime.MigrationRateChange(time=4_000, rate=0, matrix_index=(2, 0)),
            msprime.MassMigration(time=4_000, source=2, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_rhineland_cities())


def _nocturnal_workshop():
    id = "NocturnalWorkshop_1D12"
    description = "Single population with night-shift population cycles"
    long_description = """
        Single population Heinzelmaennchen model with oscillating size
        reflecting nocturnal work cycles. Modern N=300000, 500 gen ago
        N=100000, 3000 gen ago N=200000, 10000 gen ago N=50000,
        20000 gen ago N=100000.
    """
    populations = [_cologne]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch, A.",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
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
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=100_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=200_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=50_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_nocturnal_workshop())


def _cologne_expansion():
    id = "CologneExpansion_1D12"
    description = "Single population exponential growth model for Cologne"
    long_description = """
        Single population Heinzelmaennchen model with exponential growth.
        Modern N=300000, exponential growth from N=30000 starting 3000
        gen ago. Before that stable at 30000 from 20000 gen ago at
        N=100000. growth_rate = ln(300000/30000)/3000 ~ 0.000768.
    """
    populations = [_cologne]
    citations = [
        stdgrimmsim.Citation(
            author="Kopisch, A.",
            year=1836,
            doi="https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen",
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
        mutation_rate=3.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=300_000,
                growth_rate=0.000768,
                metadata=populations[0].asdict(),
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=3_000, initial_size=30_000, growth_rate=0, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=100_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_cologne_expansion())
