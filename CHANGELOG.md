# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2024-10-04 12:00:00

### Added

- Updates IRS rate threshholds and standard deduction amounts in `parameters.gov.irs.income.bracket.yaml` and in `parameters.gov.irs.deductions.standard.amount.yaml`
- Renames `WIDOW` filer type to `SURVIVING_SPOUSE`

## [0.3.0] - 2024-10-03 02:00:00

### Added

- Updates South Carolina tax logic and tests
- Replaces Mambaforge Python installer with Miniforge in GH Actions

## [0.2.9] - 2024-04-11 00:30:00

### Added

- Reinstates running `build_and_test.yml` on push after merge.
- Limits `docs_check.yml` to only run on pull request commits.
- Updates some tags in `README.md.`

## [0.2.8] - 2024-04-10 22:30:00

### Added

- Limits `build_and_test.yml` GH Action to pull requests and no pushes on merge. It also limits the codecov run to the Linux-OS tests on the latest version of Python (currently Python 3.11).

## [0.2.7] - 2024-04-10 16:00:00

### Added

- Limits the policyengine-core dependency in `setup.py` to be less than v. 2.9.

## [0.2.6] - 2023-11-14 17:00:00

### Added

- Updates Montana tax logic.

## [0.2.5] - 2023-10-24 22:00:00

### Added

- Updated environment.yml and build_and_test.yml to allow for python 3.11
- Updated Virginia tax logic with correct mapping from federal filing status to state filing status.

## [0.2.4] - 2023-10-24 10:00:00

### Added

- Fixed circularity in CO tax logic
- Fixed circularity in MO tax logic

## [0.2.3] - 2023-10-13 16:00:00

### Added

- added three files `prior_year_state_income_tax_paid.py`, `prior_year_local_income_tax_paid.py`, and `sales_or_prior_year_state_and_local_income_tax.py`
- adjusted `salt_deduction.py` to calculate based on the added variables above

## [0.2.2] - 2023-10-13 03:30:00

### Added

- Updates files from PolicyEngine-US v0.500.0 (e4a95733baafca0a7bec9ae79e96797416a4d237)

## [0.2.1] - 2023-10-09 02:00:00

### Added

- Updates two files `la_nonrefundable_childcare.py` and `in_unemployment_compensation_deduction.py` that need a `min()` reference updated to `min_()`

## [0.2.0] - 2023-10-09 01:30:00

### Added

- Updates the Python version to 3.10 in `environment.yml`, `setup.py`, `README.md`, `build_and_test.yml`, `deploy_docs.yml`, `docs_check.yml`, and `publish_to_pypi.yml`.
- Adds back the Windows CI tests to `build_and_test.yml`. See Issue #49.
- Updates to `numpy>=1.24,<1.24` and `policyengine-core>=2.8,<3` in `setup.py`. This change is what enabled the update to Python 3.10 and came from [PR #117](https://github.com/PolicyEngine/policyengine-core/pull/117) to `policyengine-core`.

## [0.1.5] - 2023-09-20 17:00:00

### Added

- Updated `README.md` and its badges.

## [0.1.4] - 2023-09-20 16:00:00

### Added

- Added Louisiana state income tax logic with credits and refunds

## [0.1.3] - 2023-09-19 12:00:00

### Added

- Updates the GH Actions files and adds two dependencies to `setup.py`
- Updates in PR #50 that updates the SNAP and TANF documentation
- Updates in PR #33 that update the VA tax logic
- Updates in PR #32 that update the MN tax logic

## [0.1.2] - 2023-07-31 18:22:17

### Added

- Updates the NumPy version in `setup.py` to be `numpy<=1.20.3` in order to be compatible with the `matplotlib` package (see [this link](https://matplotlib.org/stable/devel/min_dep_policy.html#list-of-dependency-versions)). This change should solve the `windows-latest` GitHub Action test failure from merged PR
- Updates `fiscalsim_us/data/datasets/README.md`
- Adds `abolish` parameters in `additional_parameters.yaml` file

## [0.1.1] - 2023-07-21 05:58:19

### Added

- Added documentation to the Jupyter Book for the Supplemental Nutrition Assistance Program (SNAP), formerly known as food stamps
- Added bibliographic references to the `FiscalSim-US_references.bib` file

## [0.1.0] - 2023-06-21 07:27:51

### Added

- Updates files from PolicyEngine-US v0.335.1

## [0.0.12] - 2023-06-14 15:42:49

### Changed

- Updated the value for the Kansas standard deduction amount for Widow filer types.

## [0.0.11] - 2023-06-04 07:47:45

### Changed

- Updates the `README.md`, `Makefile`, and GitHub Action `push.yaml`
- Makes many updates to the `./docs/` documentation directory

## [0.0.10] - 2023-05-19 01:51:04

### Fixed

- Fixes an error in the `setup.py` classifier description

## [0.0.9] - 2023-05-19 00:28:11

### Added

- Update the `pr.yaml` and `push.yaml` GitHub Action files. Also adds a "Check version" action to the `pr.yaml` file and adds "Update versioning" and "Publish" [to PyPI] actions to the `push.yaml` file.
- Adds small example `changelog_entry.yaml` text to `CONTRIBUTING.md`
- Adds small update to the language in `README.md`
- Manually updates the `changelog.yaml` file so it could be up-to-date for the automatic updating
- Adds small descriptor updates in `setup.py`
- Updates `README.md` badge

## [0.0.8] - 2023-04-27 20:00:00

### Added

- Updated files from PolicyEngine-US v0.303.1

## [0.0.7] - 2023-04-17 10:00:00

### Added

- Updated files from PolicyEngine-US v0.293.1

## [0.0.6] - 2023-04-15 22:40:00

### Added

- Updated files from PolicyEngine-US v0.252.0
- This PR updates the pinned version of policyengine-core
- This PR creates skip commands for the `test_microsim.py` test and three tests in `test_cps.py`

## [0.0.5] - 2023-04-13 12:00:00

### Added

- Updated files from PolicyEngine-US v0.251.1

## [0.0.4] - 2023-03-03 10:27:00

### Added

- Updated files from PolicyEngine-US v0.220.0

## [0.0.3] - 2023-02-10 14:30:00

### Added

- Adds a `fiscalsim_us/parameters/gov/states/ut/README.md` that details specific approaches taken with the Utah tax form.
- Adds all the Utah parameters to the ``fiscalsim_us/parameters/gov/states/ut` directory.
- Adds a `fiscalsim_us/variables/gov/states/README.md` that details the steps to adding a state tax logic to the model.
- Adds all the Utah variables to the ``fiscalsim_us/parameters/gov/states/ut` directory.
- Updates the `state_income_tax.py` and `state_income_tax_before_refundable_credits.py` files with the appropriate Utah variables in the `/fiscalsim_us/variables/gov/states/tax/income/` directory.
- Updates the `household_refundable_tax_credits.py` and `household_tax_before_refundable_credits.py` files with the appropriate Utah variables in the `/fiscalsim_us/variables/household/income/household/` directory.
- Sets the default value to `False` in `/fiscalsim_us/variables/household/expense/health/has_marketplace_health_coverage.py`
- `black` and `linecheck` formatted all new `.py` files.
- `make documentation` command still errors out. I need to fix the documentation.

## [0.0.2] - 2023-02-07 02:30:00

### Added

- Updated files from PolicyEngine-US v0.211.0
- Current PolicyEngine-Core version is v1.12.1

## [0.0.1] - 2022-10-24 06:40:00

### Added

- reduced the key dependencies to just `policyengine-core` instead of `openfisca-core` and `openfisca-tools`
- made `fiscalsim-us` compliant with Python 3.9

## [0.0.0] - 2022-09-28 15:59:00

### Added

- First prototype version based off of openfisca-us and tax-calculator.


[0.3.1]: https://github.com/TheCGO/fiscalsim-us/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.9...v0.3.0
[0.2.9]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.8...v0.2.9
[0.2.8]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.7...v0.2.8
[0.2.7]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.6...v0.2.7
[0.2.6]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.5...v0.2.6
[0.2.5]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.4...v0.2.5
[0.2.4]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/TheCGO/fiscalsim-us/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/TheCGO/fiscalsim-us/compare/v0.1.5...v0.2.0
[0.1.5]: https://github.com/TheCGO/fiscalsim-us/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/TheCGO/fiscalsim-us/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/TheCGO/fiscalsim-us/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/TheCGO/fiscalsim-us/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/TheCGO/fiscalsim-us/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.12...v0.1.0
[0.0.12]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.11...v0.0.12
[0.0.11]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.10...v0.0.11
[0.0.10]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.9...v0.0.10
[0.0.9]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.8...v0.0.9
[0.0.8]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/TheCGO/fiscalsim-us/compare/v0.0.0...v0.0.1
