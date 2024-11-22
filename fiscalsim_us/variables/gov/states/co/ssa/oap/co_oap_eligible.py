from fiscalsim_us.model_api import *
import numpy as np


class co_oap_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Colorado Old Age Pension Eligible"
    definition_period = YEAR
    defined_for = StateCode.CO

    def formula(person, period, parameters):
        assets = person("ssi_countable_resources", period)
        joint_claim = person("ssi_claim_is_joint", period)
        p = parameters(period).gov.states.co.ssa.oap

        assets = np.array(assets)
        joint_claim = np.array(joint_claim, dtype=bool)

        asset_limit = np.where(
            joint_claim, p.resources.couple, p.resources.single
        )

        below_asset_limit = assets <= asset_limit

        age = person("age", period)
        in_age_range = p.age_range.calc(age)

        in_age_range = np.array(in_age_range, dtype=bool)

        below_asset_limit = below_asset_limit.astype(bool)

        return below_asset_limit & in_age_range
