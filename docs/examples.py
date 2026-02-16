"""
The examples used in the tutorial section.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import stdgrimmsim  # noqa: E402


def generic_models_example():
    species = stdgrimmsim.get_species("DagHyd")
    contig = species.get_contig(length=10_000)
    model = species.get_demographic_model("InnsmouthDecline_1M27")
    samples = {"DeepOnes": 5}
    engine = stdgrimmsim.get_default_engine()
    ts = engine.simulate(model, contig, samples)
    print("num_trees =", ts.num_trees)
    print("num_sites =", ts.num_sites)


generic_models_example()
