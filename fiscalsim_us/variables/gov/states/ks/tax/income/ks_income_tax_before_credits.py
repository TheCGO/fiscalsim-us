from fiscalsim_us.model_api import *


class ks_income_tax_before_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS income tax (before credits)"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        taxable_income = tax_unit("ks_taxable_income", period)
        filing_status = tax_unit("filing_status", period)
        status = filing_status.possible_values

        rates = parameters(period).gov.states.ks.tax.income
        joint = rates.joint
        non_joint = rates.non_joint

        if filing_status == status.JOINT:
            return joint.calc(taxable_income)
        
        else:
            return non_joint.calc(taxable_income)
