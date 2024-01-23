from fiscalsim_us.model_api import *


class ar_total_income(Variable):
    "Line 23 of AR1000F"
    value_type = float
    entity = Person
    label = "Total income"
    unit = USD
    documentation = "Total income, as defined in the Arkansas state Tax Form."
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR

    def formula(person, period, parameters):
        sources = parameters(period).gov.states.ar.tax.income.income_sources
        ira_exemption = parameters(period).gov.states.ar.tax.income.rates.ira_exemption
        retirement_sources = parameters(period).gov.states.ar.tax.income.retirement_sources
        total = 0
        not_dependent = ~person("is_tax_unit_dependent", period)
        for source in sources:
            # Add positive values only - losses are deducted later.
           total += where(source in retirement_sources,  not_dependent * max_(0, add(person, period, [source])-ira_exemption),not_dependent * max_(0, add(person, period, [source])))
            
        return total
    