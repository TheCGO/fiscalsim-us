from fiscalsim_us.model_api import *


class ar_personal_credit(Variable):
    """
    Lines 7 & 34 on Arkansas 2022 Individual Income Tax return form AR1000F.
    """

    value_type = float
    entity = TaxUnit
    label = "AR personal tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        gov = parameters(period).gov
        ar_personal_credit_amount = gov.states.ar.tax.income.credits.personal.personal_credit_amount
        ar_dependents_credit_amount = gov.states.ar.tax.income.credits.personal.dependents
        ar_qual_dependents_credit_amount = gov.states.ar.tax.income.credits.personal.qual_dependents_credit_amount
        