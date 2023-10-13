from fiscalsim_us.model_api import *


class state_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "state income tax"
    unit = USD
    definition_period = YEAR
    adds = [
        # state income tax variables listed in alphabetical order:
        "ca_income_tax",
        # "co_income_tax",  --- activating will cause circular logic errors
        # "dc_income_tax",  --- activating will cause circular logic errors
        # "ia_income_tax",  --- activating will cause circular logic errors
        "il_income_tax",
        "in_income_tax",
        "ks_income_tax",
        "ky_income_tax",
        # "la_income_tax",  --- activating will cause circular logic errors
        # "ma_income_tax",  --- activating will cause circular logic errors
        # "md_income_tax",  --- activating will cause circular logic errors
        # "me_income_tax",  --- activating will cause circular logic errors
        "mn_income_tax",
        "mt_income_tax",
        # "mo_income_tax",  --- activating will cause circular logic errors
        "nc_income_tax",
        # "nd_income_tax",  --- activating will cause circular logic errors
        # "ne_income_tax",  --- activating will cause circular logic errors
        "nh_income_tax",
        "nj_income_tax",
        # "nm_income_tax",  --- activating will cause circular logic errors
        # "ny_income_tax",  --- activating will cause circular logic errors
        # "ok_income_tax",  --- activating will cause circular logic errors
        # "or_income_tax",  --- activating will cause circular logic errors
        "pa_income_tax",
        "ri_income_tax",
        # "va_income_tax",  --- temporarily deactivated until change if to where
        # "ut_income_tax",  --- temporarily deactivated until change if to where
        "wa_income_tax",
        "wi_income_tax",
    ]

    def formula(tax_unit, period, parameters):
        if parameters(period).simulation.reported_state_income_tax:
            spm_unit = tax_unit.spm_unit
            person = spm_unit.members
            is_head = person("is_tax_unit_head", period)
            total_tax_unit_heads = spm_unit.sum(is_head)
            spm_unit_state_tax = spm_unit(
                "spm_unit_state_tax_reported", period
            )
            return where(
                total_tax_unit_heads > 0,
                spm_unit_state_tax / total_tax_unit_heads,
                0,
            )
        else:
            return add(tax_unit, period, state_income_tax.adds)
