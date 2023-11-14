from fiscalsim_us.model_api import *


class va_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "va net amount of tax line 18 form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        rates = parameters(period).gov.states.va.tax.income.va_tax_rates
        taxable_inc = tax_unit("va_taxable_income", period)

        net_tax = where(taxable_inc > 0, rates.calc(taxable_inc), 0)

        return net_tax
