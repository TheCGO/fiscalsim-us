from fiscalsim_us.model_api import *


class ar_capital_loss_adjustment(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas capital loss adjustment"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000D_CapitalGains.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)

        person = tax_unit.members
        not_dependent = ~person("is_tax_unit_dependent", period)

        capital_gains = 0
        capital_gains += not_dependent * add(
            person, period, ["ar_capital_gains"]
        )

        capital_gains = tax_unit.sum(capital_gains)

        cap_loss_cap = parameters(
            period
        ).gov.states.ar.tax.income.capital_gains.capital_loss_cap[
            filing_status
        ]

        adjustment = where(
            capital_gains < -cap_loss_cap, -capital_gains - cap_loss_cap, 0
        )

        return adjustment
