from openfisca_us.model_api import *


class ks_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS adjusted gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://www.ksrevenue.gov/pdf/k-4021.pdf"

    def formula(tax_unit, period, parameters):
        federal_agi = tax_unit("adjusted_gross_income", period)
        ks_modifications = tax_unit("ks_modifications", period)

        return federal_agi + ks_modifications
