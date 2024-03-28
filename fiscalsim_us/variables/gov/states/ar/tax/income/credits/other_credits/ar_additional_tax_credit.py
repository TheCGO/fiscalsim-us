from fiscalsim_us.model_api import *


class ar_additional_tax_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas additional tax credit for qualified individuals"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)

        income = tax_unit("ar_taxable_income", period)
        p = parameters(period).gov.states.ar.tax.income.credits.other_credits

        amount = p.additional_amount

        joint_multiple = p.additional_credit_joint_multiple

        credit = amount.calc(income)

        credit = where(
            filing_status == filing_status.possible_values.JOINT,
            credit * joint_multiple,
            credit,
        )

        return credit
