from fiscalsim_us.model_api import *


class four_year_college_student(Variable):
    value_type = bool
    entity = Person
    label = "Is a four year university/college student"
    definition_period = YEAR
