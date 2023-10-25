# How to Add a State to FiscalSim US

## 1. Find the state income tax form
Find the online state income tax form for the state you are working with. For example, the 2022 state income tax form for the State of Utah is [Form TC-40](https://tax.utah.gov/forms/current/tc-40-fullpacket.pdf) and a full packet of instructions is [here](https://tax.utah.gov/forms/current/tc-40inst.pdf).

## 2. Coding up your state tax logic
It is valuable to break up the code for a particular state's tax logic into intuitive categories that correspond to the state's tax form.

## 3. Organization of the parameters tax logic
Parameters in FiscalSim US are scalars or sets of related scalars that define particular policies. For example at tax rate of 4% is a policy parameter that we would specify in the parameters folder as a scalar and allow that parameter to be changed in policy reforms. The parameters in FiscalSim US follow the OpenFisca convention of being in `.yaml` files. These are data files that are very simple and hierarchical. These files allow for parameter names, descriptions, multiple values associated with multiple dates, and significant amounts of metadata including references, URLs, and labels.

For a state tax logic, the parameters associated with that tax logic are all the scalar values that characterize the relevant state income tax policy. Examples, include tax rates, income thresholds, EITC match rates, phase-out and phase-in rates, and exemption amounts.

The Utah state income tax logic parameters are in the [`fiscalsim_us/parameters/gov/state/ut`](https://github.com/TheCGO/fiscalsim-us/tree/main/fiscalsim_us/parameters/gov/states/ut) folder.
* At the top level of this folder is a [`README.md`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/parameters/gov/states/ut/README.md) file that provides notes regarding details of how that state's tax logic parameters are organized and any exclusions, simplifications, or changes that were made.
* Below that folder is the [`tax/income`](https://github.com/TheCGO/fiscalsim-us/tree/main/fiscalsim_us/parameters/gov/states/ut/tax/income) subfolder.
* This folder contains a [`rate.yaml`](), that specifies the different flat tax rates over time and their respective effective start dates.
* At this level, there is a subfolder called [`credits/taxpayer_credit`](https://github.com/TheCGO/fiscalsim-us/tree/main/fiscalsim_us/parameters/gov/states/ut/tax/income/credits/taxpayer_credit). This folder contains `.yaml` files for personal exemption amounts, credit rates, phaseout thresholds, and phaseout rates.

Although one could simply list all the parameter `.yaml` files in a single folder, we suggest organizing the parameter files according to topics.

## 4. Organization of the variables tax logic
Variables in FiscalSim are functions and formulas of parameters and data. Variables often represent subcategories of taxes, benefits, and income definitions that are dependent upon the input data and the policy parameters. Variables also represent the tax policy because they represent how the law defines and combines the different concepts, input data, and parameters into determining things like tax liability. The variables in FiscalSim US follow the OpenFisca convention of being in `.py` files.

The tax law of each US state is different. Some states have flat taxes, and some states have progressive income tax schedules. Some states have an earned income tax match, and others do not. The variables that define each state's tax logic can be written and organized in different ways. However, some general rules apply to this process.
* It helps to associate variables with particular lines on a state's tax form. In some cases, you will want a variable to cover more than one line. And in other cases you may need multiple variables to compute one line.
* Add docstring documentation to your variables. List the form and line from which the information comes from and that the output represents.
* Although there is a lot of flexibility in how variables can be created, the following variables seem to be good practice to have in each state's tax logic. As is shown in the section below, these variables are used in calculating broader tax and benefit liability totals for a household in the model. The list below uses the state of Utah as an example with its two-letter abbreviation "ut". Any other state variables will use that state's two-letter abbreviation.
    * [`ut_total_income`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/ut/tax/income/ut_total_income.py)
    * [`ut_taxable_income`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/ut/tax/income/taxable_income/ut_taxable_income.py)
    * [`ut_income_tax`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/ut/tax/income/ut_income_tax.py)
    * [`ut_income_tax_before_refundable_credits`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/ut/tax/income/ut_income_tax_before_refundable_credits.py)
    * [`ut_refundable_credits`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/ut/tax/income/credits/refundable_credits/ut_refundable_credits.py)

## Write tests for all new variables
FiscalSim US is built on the OpenFisca platform. Tests in this repository are written as `.yaml` files saved in the [`/fiscalsim_us/tests/`](https://github.com/TheCGO/fiscalsim-us/tree/main/fiscalsim_us/tests) folder. These tests are run automatically upon any pull request commits to the main repository through the [`pr.yaml`](https://github.com/TheCGO/fiscalsim-us/blob/main/.github/workflows/pr.yaml) and [`push.yaml`](https://github.com/TheCGO/fiscalsim-us/blob/main/.github/workflows/push.yaml) GitHub Action files using the `pytest` package. These GitHub Actions run the `make test` command, which references the [`make test` portion](https://github.com/TheCGO/fiscalsim-us/blob/main/Makefile#L8) of the [`Makefile`](https://github.com/TheCGO/fiscalsim-us/blob/main/Makefile).

One should write at least one test in a `.yaml` file in the [`/fiscalsim_us/tests/`](https://github.com/TheCGO/fiscalsim-us/tree/main/fiscalsim_us/tests) folder for every variable created. These test `.yaml` files should have the same name and directory structure as the new variables being tested. For example, the test for the `ut_income_tax` variable defined in [`ut_income_tax.py`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/ut/tax/income/ut_income_tax.py) should be [`ut_income_tax.yaml`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/tests/policy/baseline/gov/states/ut/tax/income/ut_income_tax.yaml).

If you do not write tests for new variables created, the code coverage tests will catch this as a decrease in lines of code covered by continuous integration tests.

## Higher level variables to which you need to add (connect) your state variables
* [`state_income_tax`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/tax/income/state_income_tax.py): You need to add your state's `[2-letter-state-abbrev]_income_tax` variable to the list in the `adds` command.
* [`state_income_tax_before_refundable_credits.py`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/gov/states/tax/income/state_income_tax_before_refundable_credits.py): You need to add your state's `[2-letter-state-abbrev]_income_tax_before_refundable_credits` variable to the list in the `adds` command.
* [`household_refundable_tax_credits.py`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/household/income/household/household_refundable_tax_credits.py): You need to add your state's `[2-letter-state-abbrev]_refundable_credits` variable to the list in the `adds` command.
* [`household_state_income_tax.py`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/household/income/household/household_state_income_tax.py): You need to add your state's `[2-letter-state-abbrev]_income_tax_before_refundable_credits` variable to the list in the `adds` command and your state's `[2-letter-state-abbrev]_refundable_credits` variable to the list in the `subtracts` command.
* [`household_tax_before_refundable_credits.py`](https://github.com/TheCGO/fiscalsim-us/blob/main/fiscalsim_us/variables/household/income/household/household_tax_before_refundable_credits.py): You need to add your state's `[2-letter-state-abbrev]_income_tax_before_refundable_credits` variable to the list in the `adds` command.
