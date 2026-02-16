import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("MooBay")
_bayrischer_wald = stdgrimmsim.Population(
    id="BayrischerWald",
    description="Moosweiber of the Bavarian Forest (Bayrischer Wald)",
)
_oberpfalz = stdgrimmsim.Population(
    id="Oberpfalz", description="Moosweiber of the Upper Palatinate (Oberpfalz)"
)


def _bayrischer_wald_single():
    id = "BayrischerWald_1D12"
    description = "Single population Bavarian Forest Moosweib model"
    long_description = """
        Single population in the Bavarian Forest (Bayrischer Wald).
        Modern N=38000, bottleneck 4000 gen ago (N=8000),
        ancestral 30000 gen ago (N=22000).
    """
    populations = [_bayrischer_wald]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian Forest folklore",
            year=1850,
            doi="https://de.wikipedia.org/wiki/Moosweiblein",
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
                initial_size=38_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=4_000, initial_size=8_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=22_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bayrischer_wald_single())


def _bavarian_forest_oberpfalz_split():
    id = "BayrischerWaldOberpfalz_2D12"
    description = "Two population Bavarian Forest and Upper Palatinate model"
    long_description = """
        Bayrischer Wald and Oberpfalz (Upper Palatinate). Ancestral N=22000.
        Split 15000 gen ago. Bavarian Forest 38000, Oberpfalz 14000.
    """
    populations = [_bayrischer_wald, _oberpfalz]
    citations = [
        stdgrimmsim.Citation(
            author="Bavarian Forest folklore",
            year=1850,
            doi="https://de.wikipedia.org/wiki/Moosweiblein",
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
                initial_size=38_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=14_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=15_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=22_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_bavarian_forest_oberpfalz_split())
