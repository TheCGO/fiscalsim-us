from fiscalsim_us.model_api import *


class pa_total_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "PA total taxable income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2021/2021_pa-40in.pdf#page=8"
    defined_for = StateCode.PA

    def formula(tax_unit, period, parameters):
        us_gross_income = add(tax_unit, period, ["irs_gross_income"])
        p = parameters(period).gov.states.pa.tax.income
        sources = p.nontaxable_income_sources
        pa_nontaxable_income = add(tax_unit, period, sources)
        return max_(0, us_gross_income - pa_nontaxable_income)
