import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("BreSta")
_bremen = stdgrimmsim.Population(
    id="Bremen", description="Town musicians of Bremen (Grimm KHM 27)"
)
_lower_saxony = stdgrimmsim.Population(
    id="LowerSaxony", description="Lower Saxony (Niedersachsen) — road to Bremen"
)
_luneburg_heath = stdgrimmsim.Population(
    id="LuneburgHeath", description="Lüneburg Heath (Lüneburger Heide)"
)


def _bremen_single():
    id = "Bremen_1D12"
    description = "Single population Bremen town musicians model"
    long_description = """
        Single population in Bremen (Grimm KHM 27 — Die Bremer Stadtmusikanten).
        Modern N=88000, expansion 3000 gen ago (N=45000),
        ancestral 20000 gen ago (N=35000).
    """
    populations = [_bremen]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1819,
            doi="https://en.wikipedia.org/wiki/Town_Musicians_of_Bremen",
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
                initial_size=88_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=3_000, initial_size=45_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bremen_single())


def _bremen_lower_saxony_split():
    id = "BremenLowerSaxony_2D12"
    description = "Two population Bremen and Lower Saxony model"
    long_description = """
        Bremen and Lower Saxony (Niedersachsen) — the road the musicians take.
        Ancestral N=35000. Split 10000 gen ago. Bremen 88000, Lower Saxony 52000.
    """
    populations = [_bremen, _lower_saxony]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1819,
            doi="https://en.wikipedia.org/wiki/Town_Musicians_of_Bremen",
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
                initial_size=88_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=52_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=10_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bremen_lower_saxony_split())


def _bremen_three_region():
    id = "BremenLowerSaxonyLuneburg_3D12"
    description = "Three population Bremen, Lower Saxony, Lüneburg Heath"
    long_description = """
        Bremen, Lower Saxony, and Lüneburg Heath (Lüneburger Heide).
        Ancestral N=35000. Splits: Lüneburg 8000 gen ago, Lower Saxony 14000 gen ago.
    """
    populations = [_bremen, _lower_saxony, _luneburg_heath]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1819,
            doi="https://en.wikipedia.org/wiki/Town_Musicians_of_Bremen",
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
                initial_size=88_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=52_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=28_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=14_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=14_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bremen_three_region())
