from fiscalsim_us.model_api import *


class ok_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Oklahoma exemptions amount"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/past-year/2021/511-Pkt-2021.pdf"
        "https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf"
    )
    defined_for = StateCode.OK

    def formula(tax_unit, period, parameters):
        num_exemptions = tax_unit("ok_count_exemptions", period)
        p = parameters(period).gov.states.ok.tax.income.exemptions
        return num_exemptions * p.amount
