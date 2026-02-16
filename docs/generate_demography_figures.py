"""
Generate demography schematic PNGs for all catalog demographic models.

Run from the repo root (or from docs/) with stdgrimmsim and docs deps installed::

    python docs/generate_demography_figures.py

Output: docs/_static/demography/<species_id>/<model_id>.png

Requires: demesdraw, matplotlib (install with: uv sync --extra docs)
"""

from pathlib import Path
import sys

# Repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import stdgrimmsim
    import demesdraw
    import matplotlib
    matplotlib.use("Agg")
except ImportError as e:
    print("Missing dependency:", e)
    print("Install with: uv sync --extra docs")
    sys.exit(1)

OUT_DIR = Path(__file__).resolve().parent / "_static" / "demography"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n_ok = 0
    n_skip = 0
    n_fail = 0
    for species in stdgrimmsim.all_species():
        species_dir = OUT_DIR / species.id
        species_dir.mkdir(parents=True, exist_ok=True)
        for model in species.demographic_models:
            png_path = species_dir / f"{model.id}.png"
            try:
                graph = model.model.to_demes()
                ax = demesdraw.tubes(graph)
                fig = ax.get_figure()
                fig.savefig(png_path, bbox_inches="tight", dpi=100)
                import matplotlib.pyplot as plt
                plt.close(fig)
                n_ok += 1
                print(f"  {species.id}/{model.id}.png")
            except Exception as e:
                n_fail += 1
                print(f"  FAIL {species.id}/{model.id}: {e}", file=sys.stderr)
    print(f"Done: {n_ok} written, {n_fail} failed.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
