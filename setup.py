"""This file contains the fiscalsim-us package's metadata and dependencies."""

from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="fiscalsim-us",
    version="0.2.2",
    author="Center for Growth and Opportunity at Utah State University (CGO)",
    author_email="fiscalsim@thecgo.org",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    description="FiscalSim federal and state individual tax and benefit system for the US",
    keywords="tax benefit microsimulation fiscal state household individual personal",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url="https://github.com/TheCGO/fiscalsim-us",
    include_package_data=True,  # Will read MANIFEST.in
    data_files=[
        (
            "share/openfisca/openfisca-country-template",
            ["CHANGELOG.md", "LICENSE", "README.md"],
        ),
    ],
    install_requires=[
        "click==8.1.3",
        "h5py",
        "microdf_python",
        "numpy>=1.24, <1.25",
        "pandas",
        "pathlib",
        "policyengine-core>=2.8,<3",
        "pytest",
        "pytest-dependency",
        "pyyaml",
        "requests",
        "synthimpute",
        "tables",
        "tabulate",
        "tqdm",
    ],
    extras_require={
        "dev": [
            "autopep8",
            "black",
            "coverage",
            "jupyter-book",
            "jupyter",
            "linecheck",
            "markupsafe",
            "plotly",
            "bokeh>=3.1.1",
            "pydata-sphinx-theme==0.13.1",
            "setuptools",
            "sphinx",
            "sphinx-argparse",
            "sphinx-math-dollar",
            "wheel",
            "yaml-changelog",
            "survey-enhance",
        ],
    },
    python_requires=">=3.10, <3.12",
    entry_points={
        "console_scripts": [
            "fiscalsim-us = fiscalsim_us.tools.cli:main",
        ],
    },
    packages=find_packages(),
)
