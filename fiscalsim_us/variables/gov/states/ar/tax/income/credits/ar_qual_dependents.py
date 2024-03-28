from fiscalsim_us.model_api import *


class ar_qual_dependents(Variable):
    "Line 7C of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Qualifying Dependents"
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_dependent = ~person("is_tax_unit_dependent", period)
        is_disabled = ~person("is_disabled", period)

        eligible = is_dependent * is_disabled

        return tax_unit.sum(eligible)
