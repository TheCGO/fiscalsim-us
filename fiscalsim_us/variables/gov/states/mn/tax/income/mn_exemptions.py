from fiscalsim_us.model_api import *


class mn_exemptions(Variable):
    """
    Line 5 of Minnesota 2022 Individual Income Tax return from M1.
    """

    value_type = float
    entity = TaxUnit
    label = "MN exemptions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.exemptions

        fed_agi = tax_unit("adjusted_gross_income", period)
        dependents = tax_unit("tax_unit_dependents", period)
        filing_status = tax_unit("filing_status", period)
        amount_per_depend = p.dependent
        threshold = p.dependent_phaseout[filing_status]

        extra = fed_agi - threshold
        divisor = p.dependent_phase_divisor[filing_status]

        phase_out = fed_agi > threshold

        return max_(
            dependents
            * amount_per_depend
            * (1 - phase_out * np.ceil(extra / divisor) * 0.02),
            0,
        )
