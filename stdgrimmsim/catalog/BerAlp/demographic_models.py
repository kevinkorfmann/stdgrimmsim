import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("BerAlp")
_bavarian_alps = stdgrimmsim.Population(
    id="BavarianAlps", description="Berchta of the Bavarian Alps"
)
_salzburg = stdgrimmsim.Population(
    id="Salzburg", description="Berchta of Salzburg / Rauhnacht region"
)
_tyrol = stdgrimmsim.Population(id="Tyrol", description="Perchta of Tyrol (Tirol)")


def _bavarian_alps_single():
    id = "BavarianAlps_1D12"
    description = "Single population Bavarian Alps Berchta model"
    long_description = """
        Single population in the Bavarian Alps (Rauhnacht, winter spirit).
        Modern N=42000, expansion 5000 gen ago (N=20000),
        ancestral 35000 gen ago (N=15000).
    """
    populations = [_bavarian_alps]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian / Alpine folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Perchta",
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
                initial_size=42_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=5_000, initial_size=20_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=35_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bavarian_alps_single())


def _bavaria_salzburg_split():
    id = "BavarianAlpsSalzburg_2D12"
    description = "Two population Bavarian Alps and Salzburg Berchta model"
    long_description = """
        Bavarian Alps and Salzburg (Rauhnacht) populations.
        Ancestral N=15000. Split 18000 gen ago. Bavarian Alps 42000, Salzburg 22000.
    """
    populations = [_bavarian_alps, _salzburg]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian / Alpine folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Perchta",
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
                initial_size=42_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=22_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bavaria_salzburg_split())


def _alps_tyrol_split():
    id = "BavarianAlpsTyrol_2D12"
    description = "Two population Bavarian Alps and Tyrol Perchta model"
    long_description = """
        Bavarian Alps and Tyrol (Tirol). Ancestral N=15000.
        Split 12000 gen ago. Bavarian Alps 42000, Tyrol 18000.
    """
    populations = [_bavarian_alps, _tyrol]
    citations = [
        stdgrimmsim.Citation(
            author="Alpine folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Perchta",
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
                initial_size=42_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=18_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_alps_tyrol_split())
