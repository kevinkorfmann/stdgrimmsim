import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("MasLak")
_masurian_lakes = stdgrimmsim.Population(
    id="MasurianLakes", description="Lake spirits of the Masurian Lake District (Masuren)"
)
_spirdingsee = stdgrimmsim.Population(
    id="Spirdingsee", description="Spirits of the Spirdingsee (Śniardwy) region"
)
_mauersee = stdgrimmsim.Population(
    id="Mauersee", description="Spirits of the Mauersee (Mamry) region"
)


def _masurian_lakes_single():
    id = "MasurianLakes_1D12"
    description = "Single population Masurian Lake District model"
    long_description = """
        Single population in the Masurian Lake District (Masuren, East Prussia).
        Modern N=32000, expansion 4000 gen ago (N=14000),
        ancestral 22000 gen ago (N=10000).
    """
    populations = [_masurian_lakes]
    citations = [
        stdgrimmsim.Citation(
            author="Masurian folklore",
            year=1850,
            doi="https://en.wikipedia.org/wiki/Masurian_Lake_District",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=32_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=4_000, initial_size=14_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=22_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_masurian_lakes_single())


def _masurian_spirding_split():
    id = "MasurianLakesSpirdingsee_2D12"
    description = "Two population Masurian Lakes and Spirdingsee model"
    long_description = """
        Masurian Lake District and Spirdingsee (Śniardwy). Ancestral N=10000.
        Split 9000 gen ago. Masurian Lakes 32000, Spirdingsee 12000.
    """
    populations = [_masurian_lakes, _spirdingsee]
    citations = [
        stdgrimmsim.Citation(
            author="Masurian folklore",
            year=1850,
            doi="https://en.wikipedia.org/wiki/Masurian_Lake_District",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=32_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=12_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=9_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=9_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_masurian_spirding_split())


def _masurian_three_lakes():
    id = "MasurianThreeLakes_3D12"
    description = "Three population Masurian lakes: main district, Spirdingsee, Mauersee"
    long_description = """
        Three lake regions in Masuren. Ancestral N=10000. Splits: Mauersee (Mamry) 11000 gen ago,
        Spirdingsee 18000 gen ago. Masurian Lakes 32000, Spirdingsee 12000, Mauersee 15000.
    """
    populations = [_masurian_lakes, _spirdingsee, _mauersee]
    citations = [
        stdgrimmsim.Citation(
            author="Masurian folklore",
            year=1850,
            doi="https://en.wikipedia.org/wiki/Masurian_Lake_District",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=32_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=12_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=11_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_masurian_three_lakes())
