#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = "housingmodel"
DESCRIPTION = "Regression model for housing data"
URL = "missing"
EMAIL = "alexnimjli@gmail.com"
AUTHOR = "Alex Nim"
REQUIRES_PYTHON = ">=3.7.0"


# Packages that are required for this module to be executed
def list_reqs(fname="requirements.txt"):
    with open(fname) as fd:
        return fd.read().splitlines()

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
# Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / "housingmodel"
about = {}
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('old', 'notebooks')),
    #package_data is most important part to keep non-py files in your package
    #this can be used in combination with MANIFEST.ini
    package_data={'': ['*.pkl', '*.csv', '*.ipynb', 'VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
)
