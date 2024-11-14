from fiscalsim_us.model_api import *
import numpy as np


class co_state_supplement_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Colorado State Supplement Eligible"
    definition_period = YEAR
    defined_for = StateCode.CO

    def formula(person, period, parameters):
        ssi_eligible = person("is_ssi_eligible_individual", period)
        is_disabled = person("is_ssi_disabled", period)
        is_blind = person("is_blind", period)
        age = person("age", period)
        p = parameters(period).gov.states.co.ssa.state_supplement

        # Convert to boolean arrays and handle potential None or NaN values
        ssi_eligible = np.array(ssi_eligible).astype(bool)
        is_disabled = np.array(is_disabled).astype(bool)
        is_blind = np.array(is_blind).astype(bool)

        disabled_or_blind = is_disabled | is_blind
        in_age_range = p.age_range.calc(age)

        # Convert in_age_range to boolean array
        in_age_range = np.array(in_age_range).astype(bool)

        # Use bitwise & for the final operation
        return disabled_or_blind & ssi_eligible & in_age_range
