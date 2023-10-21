from fiscalsim_us.model_api import *


class mi_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Michigan exemptions"
    defined_for = StateCode.MI
    unit = USD
    definition_period = YEAR
    reference = (
        "http://legislature.mi.gov/doc.aspx?mcl-206-30",
        "https://www.legislature.mi.gov/Publications/TaxpayerGuide.pdf",
    )

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mi.tax.income.exemptions

        # Personal Exemptions & Stillborn Exemptions
        exemptions = add(
            tax_unit, period, ["tax_unit_size", "tax_unit_stillborn_children"]
        )
        personal_exemption = exemptions * p.personal

        # Disabled exemptions
        disabled_people = add(tax_unit, period, ["is_disabled"])
        disabled_exemption = disabled_people * p.disabled

        # Disabled veteran exemptions
        disabled_veterans = add(
            tax_unit, period, ["is_fully_disabled_service_connected_veteran"]
        )
        disabled_veteran_exemption = disabled_veterans * p.disabled_veteran

        # Dependent on other return exemptions
        filing_status = tax_unit("filing_status", period)
        is_dependent_on_other_return = tax_unit("dsi", period).astype(int)
        is_dependent_exemption = (
            is_dependent_on_other_return
            * p.dependent_on_other_return[filing_status]
        )

        # Total exemptions
        return (
            where(
                is_dependent_exemption == 0,
                personal_exemption,
                is_dependent_exemption,
            )
            + disabled_exemption
            + disabled_veteran_exemption
        )
