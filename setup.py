#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
import subprocess
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.

NAME = 'transbank-sdk'
MODULE_NAME = 'transbank'
DESCRIPTION = 'Transbank Python SDK'
URL = 'https://github.com/TransbankDevelopers/transbank-sdk-python'
EMAIL = 'transbankdevelopers@continuum.cl'
AUTHOR = 'Transbank'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
  "marshmallow>3, <=3.26.1",
  "requests>=2.20.0"
]

TESTS_REQUIREMENTS = [
    "pytest",
    "coverage",
    "mock",
    "requests-mock<=1.5.2"
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, MODULE_NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except FileNotFoundError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel", "--universal"], check=True)

        self.status('Uploading the package to PyPI via Twine…')
        subprocess.run(["twine", "upload", "dist/*"], check=True)

        self.status('Pushing git tags…')
        subprocess.run(["git", "tag", f"v{about['__version__']}"], check=True)
        subprocess.run(["git", "push", "--tags"], check=True)

        sys.exit()

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    tests_require=TESTS_REQUIREMENTS,
    include_package_data=True,
    license='BSD 3-clause "New" or "Revised License"',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
