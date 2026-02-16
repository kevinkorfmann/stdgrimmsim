#!/usr/bin/env python3
"""Quick test: load stdgrimmsim and run tiny simulations for several models."""
import sys
from pathlib import Path

# Allow running from repo root without installing (add parent to path)
repo = Path(__file__).resolve().parent.parent
if str(repo) not in sys.path:
    sys.path.insert(0, str(repo))


def run_one(engine, species_id, model_id, samples, length=5000, seed=42):
    import stdgrimmsim
    species = stdgrimmsim.get_species(species_id)
    model = species.get_demographic_model(model_id)
    contig = species.get_contig(length=length)
    ts = engine.simulate(model, contig, samples, seed=seed)
    return ts


def main():
    import stdgrimmsim

    engine = stdgrimmsim.get_default_engine()
    tests = [
        ("ZweBerg", "BlackForest_1D12", {"BlackForest": 4}, "Mountain Dwarves"),
        ("ZweBerg", "HarzBlackForest_2D12", {"BlackForest": 2, "Harz": 2}, "Dwarves two-pop"),
        ("NixRhe", "Rhine_1D12", {"Rhine": 4}, "Nix (Rhine)"),
        ("FraHol", "WellRealm_1D12", {"WellRealm": 4}, "Frau Holle"),
        ("SchWar", "BlackForest_1D12", {"NorthBlackForest": 4}, "Black Forest spirit"),
    ]

    for species_id, model_id, samples, label in tests:
        print(f"{label} ({species_id} / {model_id})")
        try:
            ts = run_one(engine, species_id, model_id, samples)
            print(f"  Trees: {ts.num_trees}, Sites: {ts.num_sites}, Samples: {ts.num_samples}")
        except Exception as e:
            print(f"  FAIL: {e}")
    print("Done")

if __name__ == "__main__":
    main()
