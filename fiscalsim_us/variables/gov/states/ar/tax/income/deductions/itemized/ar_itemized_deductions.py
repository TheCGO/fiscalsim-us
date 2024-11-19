from fiscalsim_us.model_api import *


class ar_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas itemized deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR3_ItemizedDeduction.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        medical_expense = add(tax_unit, period, ["medical_expense"])
        agi = tax_unit("ar_agi", period)
        medical_threshold = parameters(
            period
        ).gov.states.ar.tax.income.deductions.itemized.medical

        agi_portion = max_(0, agi * medical_threshold)

        medical_deduction = max_(0, medical_expense - agi_portion)

        real_estate_tax = add(tax_unit, period, ["real_estate_taxes"])

        # Line 6
        other_taxes = tax_unit("ar_other_taxes", period)

        interest_expense = tax_unit("interest_deduction", period)

        charitable_deduction = tax_unit("charitable_deduction", period)

        casualty_loss = add(tax_unit, period, ["casualty_loss"])

        education_deduction = tax_unit(
            "ar_post_secondary_education_tuition_deduction", period
        )

        # Miscellaneous deductions subject to AGI limit
        employee_expenses = tax_unit(
            "ar_unreimbursed_employee_expenses_deduction", period
        )
        other_limited_expenses = tax_unit("ar_other_limited_expenses", period)

        line_22 = employee_expenses + other_limited_expenses

        misc_limit_pct = parameters(
            period
        ).gov.states.ar.tax.income.deductions.itemized.miscellaneous_limit

        misc_limit = agi * misc_limit_pct

        misc_deductions = max_(0, line_22 - misc_limit)

        other_misc_deductions = tax_unit("ar_other_misc_deductions", period)

        return (
            medical_deduction
            + real_estate_tax
            + other_taxes
            + interest_expense
            + education_deduction
            + charitable_deduction
            + casualty_loss
            + misc_deductions
            + other_misc_deductions
        )
