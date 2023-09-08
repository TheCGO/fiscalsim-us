from fiscalsim_us.model_api import *


class mn_taxes_paid_deducion(Variable):
    """
    Line 10 of 2022 M1SA, Minnesota Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "MN taxes paid deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        real_estate = add(tax_unit, period, ["real_estate_taxes"])
        personal_property = tax_unit("mn_personal_property_tax", period)
        filing_status = tax_unit("filing_status", period)

        ceiling = parameters(
            period
        ).gov.states.mn.tax.income.deductions.taxes_paid_ceiling[filing_status]

        return min_(ceiling, real_estate + personal_property)
