from fiscalsim_us.model_api import *


class payroll_tax_gross_wages(Variable):
    value_type = float
    entity = Person
    label = "Gross wages and salaries for payroll taxes"
    definition_period = YEAR
    unit = USD
    adds = ["employment_income"]
