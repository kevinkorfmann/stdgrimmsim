import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("SaxErz")
_erzgebirge = stdgrimmsim.Population(
    id="Erzgebirge", description="Ore Mountains (Erzgebirge) — Saxon mining region"
)
_vogtland = stdgrimmsim.Population(
    id="Vogtland", description="Vogtland (Saxon-Bavarian border)"
)
_dresden_region = stdgrimmsim.Population(
    id="DresdenRegion", description="Dresden and upper Elbe region"
)


def _erzgebirge_single():
    id = "Erzgebirge_1D12"
    description = "Single population Erzgebirge (Ore Mountains) model"
    long_description = """
        Single population in the Erzgebirge (Saxony / Sachsen).
        Modern N=72000, bottleneck 3500 gen ago (N=18000),
        ancestral 28000 gen ago (N=40000).
    """
    populations = [_erzgebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Saxon folklore",
            year=1700,
            doi="https://en.wikipedia.org/wiki/Ore_Mountains",
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
                initial_size=72_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=3_500, initial_size=18_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=28_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_erzgebirge_single())


def _erzgebirge_vogtland_split():
    id = "ErzgebirgeVogtland_2D12"
    description = "Two population Erzgebirge and Vogtland model"
    long_description = """
        Erzgebirge and Vogtland (Saxon–Bavarian border). Ancestral N=40000.
        Split 16000 gen ago. Erzgebirge 72000, Vogtland 38000.
    """
    populations = [_erzgebirge, _vogtland]
    citations = [
        stdgrimmsim.Citation(
            author="Saxon folklore",
            year=1700,
            doi="https://en.wikipedia.org/wiki/Ore_Mountains",
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
                initial_size=72_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=38_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=16_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=16_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_erzgebirge_vogtland_split())


def _saxony_three_region():
    id = "ErzgebirgeVogtlandDresden_3D12"
    description = "Three population Erzgebirge, Vogtland, Dresden region"
    long_description = """
        Erzgebirge, Vogtland, and Dresden/upper Elbe. Ancestral N=40000.
        Splits: Dresden region 10000 gen ago, Vogtland 20000 gen ago.
    """
    populations = [_erzgebirge, _vogtland, _dresden_region]
    citations = [
        stdgrimmsim.Citation(
            author="Saxon folklore",
            year=1700,
            doi="https://en.wikipedia.org/wiki/Ore_Mountains",
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
                initial_size=72_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=38_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=10_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=20_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_saxony_three_region())
