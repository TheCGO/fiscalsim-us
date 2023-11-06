from fiscalsim_us.model_api import *


class ar_income_tax_before_non_refundable_credits(Variable):
    "Line 29 of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas income tax before non refundable credits"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2023_Final_AR1000ES.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):

        taxable_income = tax_unit("ar_taxable_income", period)
        high_income_threshold = parameters(period).gov.states.ar.tax.income.rates.regular_bracket_max
        litc = tax_unit('ar_income_tax_credit', period)

        rate = where(taxable_income < high_income_threshold, parameters(period).gov.states.ar.tax.income.rates.rates, parameters(period).gov.states.ar.tax.income.rates.high_income_rates)
        
        tax = rate.calc(taxable_income) - litc



        return tax
