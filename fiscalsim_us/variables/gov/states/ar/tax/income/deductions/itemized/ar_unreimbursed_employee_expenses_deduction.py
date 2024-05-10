from fiscalsim_us.model_api import *


class ar_unreimbursed_employee_expenses_deduction(Variable):
    """
    Line 20 of 2022 AR3, Arkansas Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "AR unreimbursed employee expenses deduction"
    unit = USD
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR2106_EmployeeBusinessExpenses.pdf"
    definition_period = YEAR
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        expenses = tax_unit("ar_unreimbursed_employee_expenses", period)

        p = parameters(period).gov.states.ar.tax.income.deductions.itemized

        multiple = p.unreimbursed_employee_expenses_multiple

        return expenses * multiple
