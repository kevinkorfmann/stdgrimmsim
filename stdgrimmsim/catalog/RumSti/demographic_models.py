import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("RumSti")
_thuringia = stdgrimmsim.Population(
    id="Thuringia", description="Rumpelstiltskin's realm (Thuringia / Thüringen)"
)
_hesse = stdgrimmsim.Population(
    id="Hesse", description="Hesse (Hessen) — Grimm heartland"
)


def _thuringia_single():
    id = "Thuringia_1D12"
    description = "Single population Thuringia Rumpelstiltskin model"
    long_description = """
        Single population in Thuringia (Grimm KHM 55 — Rumpelstilzchen).
        Modern N=48000, bottleneck 2500 gen ago (N=12000),
        ancestral 30000 gen ago (N=28000).
    """
    populations = [_thuringia]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Rumpelstiltskin",
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
                initial_size=48_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2_500, initial_size=12_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=28_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_thuringia_single())


def _thuringia_hesse_split():
    id = "ThuringiaHesse_2D12"
    description = "Two population Thuringia and Hesse (Grimm fairy-tale region)"
    long_description = """
        Thuringia and Hesse — Grimm territory. Ancestral N=28000.
        Split 15000 gen ago. Thuringia 48000, Hesse 32000.
    """
    populations = [_thuringia, _hesse]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Rumpelstiltskin",
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
                initial_size=48_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=32_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=15_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=28_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_thuringia_hesse_split())
