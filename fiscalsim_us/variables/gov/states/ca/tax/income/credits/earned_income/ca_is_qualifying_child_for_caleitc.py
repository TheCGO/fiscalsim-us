from fiscalsim_us.model_api import *


class ca_is_qualifying_child_for_caleitc(Variable):
    value_type = bool
    entity = Person
    label = "Child qualifies for CalEITC"
    definition_period = YEAR
    reference = "https://www.ftb.ca.gov/file/personal/credits/EITC-calculator/Help/QualifyingChildren"

    def formula(person, period, parameters):
        # CalEITC uses federal EITC rules regarding qualifying children
        return person("is_eitc_qualifying_child", period)
