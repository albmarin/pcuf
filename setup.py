#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "xlrd>=1.2.0",
    "pandas>=0.24.1",
    "requests>=2.21.0",
    "click>=7.0",
    "openpyxl>=2.5.12",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Alberto J. Marin",
    author_email="alberto@ajmar.in",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="A personal collection of useful and frequently used Python functions.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="pcuf",
    name="pcuf",
    packages=find_packages(include=["pcuf"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/git-albertomarin/pcuf",
    version="0.1.0",
    zip_safe=False,
)
