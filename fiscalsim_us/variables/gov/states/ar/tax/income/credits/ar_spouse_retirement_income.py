from fiscalsim_us.model_api import *


class ar_spouse_retirement_income(Variable):
    """ Line 18B, If zero, mark '65 Special' Line 7A of form AR1000F
        - taxable_pension_income
        - qualified_ira_distributions
    """
    value_type = float
    entity = TaxUnit
    label = "Arkansas Spouse retirement income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR