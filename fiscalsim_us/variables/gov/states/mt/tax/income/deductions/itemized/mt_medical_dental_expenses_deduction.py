from fiscalsim_us.model_api import *


class mt_medical_dental_expenses_deduction(Variable):
    """
    Line 1 on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana medical and dental expense deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.mt.tax.income.deductions.itemized.medical_dental
        line1a = tax_unit("mt_medical_dental_expense", period)
        line1b = tax_unit("mt_agi", period)
        line1c = line1b * p.rate

        return max_(line1c - line1a, 0)
