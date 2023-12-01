from fiscalsim_us.model_api import *


class ga_nonrefundable_credits(Variable):
    """
    Other GA nonrefundable credits. Catch all for credits not
    currently implemented. Includes:
    - Tax credits from states other than Georgia
    The following are from the IND-CR summary worksheet
    - Disabled Person Home Purchase  or Retrofit Credit
    - Georgia National Guard /Air National Guard Credit
    - Qualified Caregiving Expense Credit
    - Disaster Assistance Credit
    - Rural Physicians Credit
    - Adoption of a Foster Child Credit for Adoptions Occurring in Taxable
        Years Beginning on or After January 1, 2008 and Before January 1, 2021
    - Eligible Single-Family Residence Credit
    - Community Based Faculty Preceptor Credit
    - Adoption of a Foster Child Credit for Adoptions Occurring in Taxable
    Years Beginning on or After January 1, 2021
    - Teacher Recruitment and Retention Credit
    """

    value_type = float
    entity = TaxUnit
    label = "Georgia nonrefundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.GA
    adds = "gov.states.ga.tax.income.credits.nonrefundable"
