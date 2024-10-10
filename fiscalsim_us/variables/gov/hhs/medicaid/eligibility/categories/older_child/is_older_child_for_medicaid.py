import numpy as np
from fiscalsim_us.model_api import *


class is_older_child_for_medicaid(Variable):
    value_type = bool
    entity = Person
    label = "Older children"
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/42/1396a#l_1_D"

    def formula(person, period, parameters):
        age = person("age", period)
        ma = parameters(
            period
        ).gov.hhs.medicaid.eligibility.categories.older_child
        income = person("medicaid_income_level", period)
        is_older_child = ma.age_range.calc(age)
        state = person.household("state_code_str", period)
        income_limit = ma.income_limit[state]

        try:
            result = is_older_child & (income < income_limit)
            return result
        except Exception as e:
            print(f"Calculation failed: {str(e)}")
            print(
                f"is_older_child: type={type(is_older_child)}, value={is_older_child}"
            )
            print(f"income: type={type(income)}, value={income}")
            print(
                f"income_limit: type={type(income_limit)}, value={income_limit}"
            )

            # Convert to numpy arrays and ensure correct types
            is_older_child = np.asarray(
                is_older_child if is_older_child is not None else False
            ).astype(bool)
            income = np.asarray(income if income is not None else 0).astype(
                float
            )
            income_limit = np.asarray(
                income_limit if income_limit is not None else 0
            ).astype(float)

            # Attempt calculation again
            result = is_older_child & (income < income_limit)
            print("Calculation succeeded after type conversion")
            return result
