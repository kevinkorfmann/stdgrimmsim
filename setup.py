#!/usr/bin/env python3
from setuptools import setup

setup(
    # Set the name so that github correctly tracks reverse dependencies.
    # https://github.com/popsim-consortium/stdgrimmsim/network/dependents
    name="stdgrimmsim",
    use_scm_version={"write_to": "stdgrimmsim/_version.py"},
)
