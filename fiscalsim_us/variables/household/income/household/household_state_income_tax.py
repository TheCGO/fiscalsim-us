from fiscalsim_us.model_api import *


class household_state_income_tax(Variable):
    # This definition contains all modelled states, and exists to solve circular dependencies in state_income_tax.
    value_type = float
    entity = TaxUnit
    label = "household State tax"
    unit = USD
    definition_period = YEAR
    adds = [
        "ca_income_tax_before_refundable_credits",
        "co_income_tax_before_refundable_credits",
        "dc_income_tax_before_refundable_credits",
        "ia_income_tax_before_refundable_credits",
        "il_total_tax",
        "in_income_tax_before_refundable_credits",
        "ks_income_tax_before_refundable_credits",
        "ky_income_tax_before_refundable_credits",
        "la_income_tax_before_refundable_credits",
        "me_income_tax_before_refundable_credits",
        "ma_income_tax_before_refundable_credits",
        "md_income_tax_before_refundable_credits",
        "mn_income_tax_before_refundable_credits",
        "mt_income_tax_before_refundable_credits",
        "mo_income_tax_before_refundable_credits",
        "nc_income_tax",
        "nd_income_tax_before_refundable_credits",
        "ne_income_tax_before_refundable_credits",
        "nh_income_tax_before_refundable_credits",
        "nj_income_tax_before_refundable_credits",
        "nm_income_tax_before_refundable_credits",
        "ny_income_tax_before_refundable_credits",
        "ok_income_tax_before_refundable_credits",
        "or_income_tax_before_refundable_credits",
        "pa_income_tax",
        "ri_income_tax_before_refundable_credits",
        "ut_income_tax_before_refundable_credits",
        "va_income_tax_before_refundable_credits",
        "vt_income_tax_before_refundable_credits",
        "wa_income_tax_before_refundable_credits",
        "wi_income_tax_before_refundable_credits",
        "nyc_income_tax_before_refundable_credits",
    ]
    subtracts = [
        "ca_refundable_credits",  # California.
        "co_refundable_credits",  # Colorado
        "dc_refundable_credits",  # District of Columbia.
        "ia_refundable_credits",  # Iowa.
        "il_refundable_credits",  # Illinois.
        "in_refundable_credits",  # Indiana.
        "ks_refundable_credits",  # Kansas.
        "ky_refundable_credits",  # Kentucky.
        "la_refundable_credits",  # Louisiana.
        "ma_refundable_credits",  # Massachusetts.
        "me_refundable_credits",  # Maine.
        "md_refundable_credits",  # Maryland.
        "mn_refundable_credits",  # Minnesota.
        "mt_refundable_credits",  # Montana.
        "mo_refundable_credits",  # Missouri.
        # Skip NC, which has no refundable credits.
        "nd_refundable_credits",  # North Dakota.
        "ne_refundable_credits",  # Nebraska.
        "nh_refundable_credits",  # New Hampshire.
        "nj_refundable_credits",  # New Jersey.
        "nm_refundable_credits",  # New Mexico.
        "ny_refundable_credits",  # New York.
        "ok_refundable_credits",  # Oklahoma.
        "or_refundable_credits",  # Oregon.
        # Skip PA, which has no refundable credits.
        "ri_refundable_credits",  # Rhode Island.
        "ut_refundable_credits",  # Utah.
        "va_refundable_credits",  # Virginia.
        "vt_refundable_credits",  # Vermont.
        "wa_refundable_credits",  # Washington.
        "wi_refundable_credits",  # Wisconsin.
        # LOCAL
        "nyc_refundable_credits",  # New York City.
    ]

    def formula(tax_unit, period, parameters):
        if parameters(period).simulation.reported_state_income_tax:
            spm_unit = tax_unit.spm_unit
            total_tax_unit_heads = add(spm_unit, period, ["is_tax_unit_head"])
            spm_unit_state_tax = spm_unit(
                "spm_unit_state_tax_reported", period
            )
            return where(
                total_tax_unit_heads > 0,
                spm_unit_state_tax / total_tax_unit_heads,
                0,
            )
        else:
            return add(
                tax_unit, period, household_state_income_tax.adds
            ) - add(tax_unit, period, household_state_income_tax.subtracts)
