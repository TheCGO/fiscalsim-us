from fiscalsim_us.model_api import *


class ks_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS itemized deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/scha21.pdf"
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        federal_deductions_if_itemizing = parameters(
            period
        ).gov.irs.deductions.deductions_if_itemizing
        ks_deductions_if_itemizing = [
            deduction
            for deduction in federal_deductions_if_itemizing
            if deduction 
            not in [
                "salt_deduction", 
                "casualty_loss_deduction",
                # Exclude QBID to avoid circular reference.
                "qualified_business_income_deduction",
            ]
        ]
        return add(tax_unit, period, ks_deductions_if_itemizing)
