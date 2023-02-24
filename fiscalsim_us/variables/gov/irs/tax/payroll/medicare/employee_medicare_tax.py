from fiscalsim_us.model_api import *


class employee_medicare_tax(Variable):
    value_type = float
    entity = Person
    label = "employee-side health insurance payroll tax"
    documentation = (
        "Total liability for employee-side health insurance payroll tax."
    )
    definition_period = YEAR
    unit = USD

    def formula(person, period, parameters):
        rate = parameters(period).gov.irs.payroll.medicare.rate.employee
        return rate * person("payroll_tax_gross_wages", period)
