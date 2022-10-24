"""This file contains your country package's metadata and dependencies."""

from setuptools import find_packages, setup

setup(
    name="FiscalSim-US",
    version="0.0.0",
    author="Center for Growth and Opportunity at Utah State University (CGO)",
    author_email="revans@thecgo.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    description="FiscalSim US and state tax and benefit system",
    keywords="benefit microsimulation social tax",
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
        "h5py",
        "microdf_python",
        "policyengine-core >= 1.3.0",
        "pandas",
        "pathlib",
        "pytest",
        "pytest-dependency",
        "pyyaml",
        "requests",
        "synthimpute",
        "tables",
        "tqdm",
        "click>=8.0.0",
        "tabulate",
    ],
    extras_require={
        "dev": [
            "autopep8 >= 1.5.4, < 2.0.0",
            "black",
            "coverage",
            "jupyter-book",
            "plotly",
            "pytest",
            "setuptools",
            "wheel",
            "yaml-changelog>=0.1.7",
            "linecheck",
            "furo<2023",
            "markupsafe==2.0.1",
            "sphinx>=4.5.0,<5",
            "sphinx-argparse>=0.3.2,<1",
            "sphinx-math-dollar>=1.2.1,<2",
        ],
    },
    python_requires=">=3.7,<3.10",
    entry_points={
        "console_scripts": [
            "fiscalsim-us = policyengine_us.tools.cli:main",
        ],
    },
    packages=find_packages(),
)
