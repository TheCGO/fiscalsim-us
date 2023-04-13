# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] = 2023-04-13 12:00:00

### Changed

- Updated files from PolicyEngine-US v0.251.1

## [0.0.4] = 2023-03-03 10:27:00

### Changed

- Updated files from PolicyEngine-US v0.220.0

## [0.0.3] = 2023-02-10 14:30:00

### Changed

- Adds a `fiscalsim_us/parameters/gov/states/ut/README.md` that details specific approaches taken with the Utah tax form.
- Adds all the Utah parameters to the ``fiscalsim_us/parameters/gov/states/ut` directory.
- Adds a `fiscalsim_us/variables/gov/states/README.md` that details the steps to adding a state tax logic to the model.
- Adds all the Utah variables to the ``fiscalsim_us/parameters/gov/states/ut` directory.
- Updates the `state_income_tax.py` and `state_income_tax_before_refundable_credits.py` files with the appropriate Utah variables in the `/fiscalsim_us/variables/gov/states/tax/income/` directory.
- Updates the `household_refundable_tax_credits.py` and `household_tax_before_refundable_credits.py` files with the appropriate Utah variables in the `/fiscalsim_us/variables/household/income/household/` directory.
- Sets the default value to `False` in `/fiscalsim_us/variables/household/expense/health/has_marketplace_health_coverage.py`
- `black` and `linecheck` formatted all new `.py` files.
- `make documentation` command still errors out. I need to fix the documentation.

## [0.0.2] = 2023-02-07 02:30:00

### Changed

- Updated files from PolicyEngine-US v0.211.0
- Current PolicyEngine-Core version is v1.12.1

## [0.0.1] - 2022-10-24 06:40:00

### Changed

- reduced the key dependencies to just `policyengine-core` instead of `openfisca-core` and `openfisca-tools`
- made `fiscalsim-us` compliant with Python 3.9

## [0.0.0] - 2022-09-28 15:59:00

### Initial file upload

- This model is build from the foundation of `policyengine-us` and `tax-calculator` model repositories.
