class ar_cdcc_qualified_dependent(Variable):
    value_type = bool
    entity = Person
    label = "Qualifying dependent for Arkansas CDCC"
    documentation = "Whether this person qualifies as a dependent for the child and dependent care credit."
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR2441_Child_andDependentCareExpenses_Instructions.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ar.tax.income.credits.cdcc
        meets_age_criteria = person("age", period) < p.child_age
        incapable_of_self_care = person("incapable_of_self_care", period)
        is_dependent = person("is_tax_unit_dependent", period)
        is_spouse = person("is_tax_unit_spouse", period)
        dependent_or_spouse = is_dependent | is_spouse
        return meets_age_criteria | (
            dependent_or_spouse & incapable_of_self_care
        )