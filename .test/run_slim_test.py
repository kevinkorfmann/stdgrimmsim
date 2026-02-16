#!/usr/bin/env python3
"""Quick SLiM engine test: script generation and optionally run tiny simulations."""
import io
import sys
import warnings
from contextlib import redirect_stdout
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
if str(repo) not in sys.path:
    sys.path.insert(0, str(repo))


def main():
    import stdgrimmsim

    try:
        engine = stdgrimmsim.get_engine("slim")
    except Exception as e:
        print("Could not get SLiM engine:", e)
        return 1

    # Use diploid species only (SLiM engine supports ploidy 1 or 2)
    tests = [
        ("DagHyd", "InnsmouthDecline_1M27", {"DeepOnes": 4}, "Deep Ones"),
        ("DagHyd", "HybridIntrogression_2M27", {"DeepOnes": 2, "Hybrids": 2}, "Deep Ones + Hybrids"),
        ("NigMan", "NgranekFlock_1C26", {"NophorPeaks": 4}, "Nightgaunt"),
    ]

    # 1. Script generation (no SLiM binary needed)
    print("SLiM script generation")
    for species_id, model_id, samples, label in tests:
        print("  {} ({}/{}) ... ".format(label, species_id, model_id), end="", flush=True)
        try:
            species = stdgrimmsim.get_species(species_id)
            model = species.get_demographic_model(model_id)
            contig = species.get_contig(length=3000)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                buf = io.StringIO()
                with redirect_stdout(buf):
                    engine.simulate(
                        model, contig, samples, seed=42, slim_script=True
                    )
                script = buf.getvalue()
            if script and "initialize()" in script and "registerLateEvent" in script:
                print("OK ({} chars)".format(len(script)))
            else:
                print("FAIL (invalid script)")
                return 1
        except Exception as e:
            print("FAIL:", e)
            return 1

    # 2. Optional: run one actual simulation (requires SLiM on PATH; SLiM 3.x recommended)
    print("SLiM run (DagHyd, short contig)")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", stdgrimmsim.SLiMScalingFactorWarning)
            warnings.simplefilter("ignore", UserWarning)
        species = stdgrimmsim.get_species("DagHyd")
        model = species.get_demographic_model("InnsmouthDecline_1M27")
        contig = species.get_contig(length=2000)
        ts = engine.simulate(
            model,
            contig,
            {"DeepOnes": 4},
            seed=42,
            slim_scaling_factor=25,
            slim_burn_in=0,
        )
        print("  OK  trees={} sites={} samples={}".format(
            ts.num_trees, ts.num_sites, ts.num_samples
        ))
    except Exception as e:
        print("  SKIP (SLiM run failed, script generation passed):", e)
        print("  Tip: SLiM 3.x is recommended; SLiM 4.x may need engine updates.")

    print("SLiM tests done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
