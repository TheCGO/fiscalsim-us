from fiscalsim_us.model_api import *


class person_id(Variable):
    value_type = int
    entity = Person
    label = "Unique reference for this person"
    definition_period = YEAR

    def formula(person, period, parameters):
        return np.arange(len(person("age", period)))
