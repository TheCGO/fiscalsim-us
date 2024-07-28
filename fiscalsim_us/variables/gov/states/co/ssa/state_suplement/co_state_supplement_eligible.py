from fiscalsim_us.model_api import *


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

        # Handle potential None or NaN values
        ssi_eligible = np.nan_to_num(ssi_eligible, nan=False)
        is_disabled = np.nan_to_num(is_disabled, nan=False)
        is_blind = np.nan_to_num(is_blind, nan=False)
        
        disabled_or_blind = is_disabled | is_blind
        in_age_range = p.age_range.calc(age)
        
        # Handle potential None or NaN in in_age_range
        in_age_range = np.nan_to_num(in_age_range, nan=False)

        return disabled_or_blind & ssi_eligible & in_age_range
