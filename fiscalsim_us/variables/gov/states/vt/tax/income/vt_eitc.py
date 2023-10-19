from fiscalsim_us.model_api import *


class vt_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "Vermont earned income tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://tax.vermont.gov/sites/tax/files/documents/IN-112-2022.pdf#page=1"
    defined_for = StateCode.VT

    def formula(tax_unit, period, parameters):
        eitc = tax_unit("earned_income_tax_credit", period)
        rate = parameters(period).gov.states.vt.tax.income.credits.eitc.match
        return eitc * rate
