"""
Pytest configuration for stdgrimmsim.
"""

import pathlib

# Detect SLiM version; skip test_slim_engine if SLiM 4.x (API incompatible with generated scripts)
def _get_slim_major():
    try:
        import stdgrimmsim
        engine = stdgrimmsim.get_engine("SLiM")
        if engine is None:
            return 0
        ver = engine.get_version()
        return int(ver.split(".")[0]) if ver else 0
    except Exception:
        return 0

SLIM_MAJOR = _get_slim_major()

# Species IDs in the stdgrimmsim catalog (German folklore)
CATALOG_SPECIES = {
    "ZweBerg",
    "NixRhe",
    "RueHar",
    "FraHol",
    "LorRhe",
    "SchWar",
    "WilJae",
    "WerWol",
    "LinDra",
    "KobHau",
    "HeiCol",
    "FeeFlu",
    "ErlKoe",
    "AlpNac",
    "WolBay",
    "BerAlp",
    "MooBay",
    "PukPru",
    "OstBal",
    "MasLak",
    "RumSti",
    "SieRab",
    "BreSta",
    "SaxErz",
    "PomBal",
    "AscPut",
}

# Reference species for test_cli / test_slim_engine (needs dem model + pops)
REFERENCE_SPECIES_ID = "ZweBerg"
REFERENCE_POP = "BlackForest"
REFERENCE_MODEL = "BlackForest_1D12"
REFERENCE_CONTIG = "1"
REFERENCE_LENGTH = 1_000_000

# Test modules that target species not in the catalog (from stdpopsim); skip them.
SKIP_SPECIES_TEST_MODULES = {
    "test_AraTha",
    "test_BosTau",
    "test_DroMel",
    "test_DroSec",
    "test_EscCol",
    "test_HomSap",
    "test_PanTro",
    "test_RatNor",
    "test_StrAga",
    "test_SusScr",
}


def _catalog_has_species():
    """Species IDs that must be in catalog for test_cli / test_slim_engine."""
    import stdgrimmsim

    return {s.id for s in stdgrimmsim.all_species()}


def pytest_ignore_collect(collection_path, config):
    """Skip test modules for species not in the catalog (e.g. test_HomSap.py)."""
    path = pathlib.Path(collection_path)
    if path.suffix == ".py" and path.name.startswith("test_"):
        stem = path.stem
        if stem in SKIP_SPECIES_TEST_MODULES:
            return True
        # Skip SLiM engine tests when SLiM 4.x is installed (API incompatible)
        if stem == "test_slim_engine" and SLIM_MAJOR >= 4:
            return True
        # test_cli and test_slim_engine run if catalog has at least one species
        if stem in ("test_cli", "test_slim_engine"):
            catalog_ids = _catalog_has_species()
            if len(catalog_ids) == 0:
                return True
        if stem in ("test_genomes", "test_genetic_maps", "test_annotations"):
            catalog_ids = _catalog_has_species()
            if len(catalog_ids) == 0:
                return True
        if stem in ("test_maintenance", "test_dfes"):
            return False
        # test_SpeciesId.py -> SpeciesId (dynamic species tests)
        if len(stem) > 5:
            maybe_species = stem[5:]
            if maybe_species not in CATALOG_SPECIES and maybe_species[0].isupper():
                return True
    return False
