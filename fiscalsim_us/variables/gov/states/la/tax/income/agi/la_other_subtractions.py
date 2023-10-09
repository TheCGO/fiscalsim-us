from fiscalsim_us.model_api import *


class la_other_subtractions(Variable):
    """
    Other subtractions from louisiana taxable income.
    These include the following exemptions from income with
    the associated codes:
    05E – Other Retirement Benefits
    06E – Annual Retirement Income Exemption for Taxpayers 65
    Years of Age or Older
    08E – Native American Income
    09E – START Savings Program Contribution
    10E – Military Pay Exclusion
    11E – Road Home
    13E – Recreation Volunteer
    14E – Volunteer Firefighter
    16E – Voluntary Retrofit Residential Structure
    17E – Elementary and Secondary School Tuition
    18E – Educational Expenses for Home-Schooled Children
    19E – Educational Expenses for a Quality Public Education
    20E – Capital Gain from Sale of Louisiana Business
    21E – Employment of Certain Qualified Disabled Individuals
    22E – S Bank Shareholder Income Exclusion
    23E – Entity Level Taxes Paid to Other States
    24E – Pass–Through Entity Exclusion
    25E – IRC 280C Expense
    27E – COVID-19 Relief Benefits
    28E – START K12 Savings Program Contributions
    29E – Digital Nomad
    30E – Certain Adoptions
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana other subtractions from AGI"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
