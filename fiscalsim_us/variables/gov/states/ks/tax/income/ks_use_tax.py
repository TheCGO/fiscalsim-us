from fiscalsim_us.model_api import *


class ks_use_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "CA Use Tax"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2021/2021_pa-40in.pdf#page=22"
    defined_for = StateCode.CA

    def formula(tax_unit, period, parameters):
        income = tax_unit("ks_agi", period)
        p = parameters(period).gov.states.ks.tax.income.use_tax
        # Compute main amount, a dollar amount based on KS AGI.
        main_amount = p.main.calc(income)
        # Switches to a percentage of income above the top main threshold.
        additional = income * p.multiplier
        
        if income > p.threshold:

            return main_amount

        else:

            return additional
        

