from fiscalsim_us.model_api import *


class marginal_tax_rate(Variable):
    label = "marginal tax rate"
    documentation = "Fraction of marginal income gains that do not increase household net income."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "/1"

    def formula(person, period, parameters):
        netinc_base = person.household("household_net_income", period)
        delta = parameters(period).simulation.marginal_tax_rate_delta
        adult_count = parameters(period).simulation.marginal_tax_rate_adults
        sim = person.simulation
        mtr_values = np.zeros(person.count, dtype=np.float32)
        adult_indexes = person("adult_index", period)
        for adult_index in range(1, 1 + adult_count):
            alt_sim = sim.get_branch(f"mtr_for_adult_{adult_index}")
            for variable in sim.tax_benefit_system.variables:
                if variable not in sim.input_variables:
                    alt_sim.delete_arrays(variable)
            mask = adult_index == adult_indexes
            alt_sim.set_input(
                "employment_income",
                period,
                person("employment_income", period) + mask * delta,
            )
            alt_person = alt_sim.person
            netinc_alt = alt_person.household("household_net_income", period)
            increase = netinc_alt - netinc_base
            mtr_values += where(mask, 1 - increase / delta, 0)
        return mtr_values


class adult_index(Variable):
    value_type = int
    entity = Person
    label = "Index of adult in household"
    definition_period = YEAR

    def formula(person, period, parameters):
        return (
            person.get_rank(
                person.household,
                -person("age", period),
                condition=person("is_adult", period),
            )
            + 1
        )
