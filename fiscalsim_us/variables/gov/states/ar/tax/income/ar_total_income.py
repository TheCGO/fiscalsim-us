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
        loss_cap = parameters(period).gov.states.ar.tax.income.capital_gains.capital_loss_cap
        total = 0
        not_dependent = ~person("is_tax_unit_dependent", period)
        for source in sources:
            print(source)
            print("Processing source:", source)
            print("Is source in retirement_sources?", source in retirement_sources)
            # Add positive values only - losses are deducted later.
            amount = add(person, period, source)
            total += where(source in retirement_sources,  not_dependent * max_(0, amount -ira_exemption),not_dependent * max_(0,amount))
            print("total: ", total)

        return total