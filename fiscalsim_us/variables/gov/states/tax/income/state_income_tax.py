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
        "dc_income_tax",
        "ia_income_tax",
        "il_income_tax",
        "in_income_tax",
        "ks_income_tax",
        "ky_income_tax",
        "la_income_tax",
        "ma_income_tax",
        "md_income_tax",
        "me_income_tax",
        "mn_income_tax",
        "mt_income_tax",
        # "mo_income_tax",  --- activating will cause circular logic errors
        "nc_income_tax",
        "nd_income_tax",
        "ne_income_tax",
        "nh_income_tax",
        "nj_income_tax",
        "nm_income_tax",
        "ny_income_tax",
        "ok_income_tax",
        "or_income_tax",
        "pa_income_tax",
        "ri_income_tax",
        # "va_income_tax",  --- temporarily deactivated until change if to where
        "ut_income_tax",
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
