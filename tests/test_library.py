"""Smoke tests: every library module imports and its key public API is intact.

Guarantees the ``src/sci_demographic_collapse`` package is importable and its public
functions/classes still exist, so a broken import or a renamed symbol fails CI. Runs on
CPU and touches neither the dataset nor a GPU - it exercises the pure-python numerics only.
"""
import importlib
import pkgutil

import pytest

import sci_demographic_collapse as pkg

MODULES = [
    "config",
    "coremodel",
    "dataset",
    "emergent",
    "features",
    "plots",
    "proxies",
]


def test_package_imports():
    assert pkg.__name__ == "sci_demographic_collapse"


@pytest.mark.parametrize("mod", MODULES)
def test_module_imports(mod):
    importlib.import_module(f"sci_demographic_collapse.{mod}")


def test_every_submodule_imports():
    """Import every submodule discovered under the package - catches a newly added broken file."""
    for info in pkgutil.iter_modules(pkg.__path__):
        importlib.import_module(f"{pkg.__name__}.{info.name}")


def test_emergent_api_and_numerics():
    from sci_demographic_collapse.emergent import EmergentModel, fec, quantum

    assert callable(EmergentModel)
    # pure-python numerics run without the dataset or a GPU
    assert quantum(0.9, 0.07, 1.5) == pytest.approx(0.9 * (1 - 0.07) * 1.5)
    assert fec(30.0) == pytest.approx(1.0)
    assert fec(35.0) < 1.0


def test_proxies_api_and_numerics():
    from sci_demographic_collapse.proxies import PROXIES, education_cost_multiplier

    assert len(PROXIES) >= 6
    assert education_cost_multiplier(0.1, 0.2) == pytest.approx(0.1 * (1 + 0.22 * 0.2))
    with pytest.raises(ValueError):
        education_cost_multiplier(1.5, 0.2)
