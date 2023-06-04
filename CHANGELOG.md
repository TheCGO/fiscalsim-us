# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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



[0.0.11]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.10...0.0.11
[0.0.10]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.9...0.0.10
[0.0.9]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.8...0.0.9
[0.0.8]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.7...0.0.8
[0.0.7]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.6...0.0.7
[0.0.6]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.5...0.0.6
[0.0.5]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.4...0.0.5
[0.0.4]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.3...0.0.4
[0.0.3]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/TheCGO/fiscalsim-us/compare/0.0.0...0.0.1

