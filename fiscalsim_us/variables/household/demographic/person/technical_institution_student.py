from fiscalsim_us.model_api import *


class technical_institution_student(Variable):
    value_type = bool
    entity = Person
    label = "Is a student of a technical institute"
    definition_period = YEAR
