from fiscalsim_us.model_api import *


class alt_energy_device_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Idaho Alternative Energy Device Deduction"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.id.tax.income.subtractions.id_alt_energy_device_deduction
        limit = p.alt_energy_device_deduction_limit
        cost_19 = tax_unit("alt_energy_device_cost_2019", period)
        cost_20 = tax_unit("alt_energy_device_cost_2020", period)
        cost_21 = tax_unit("alt_energy_device_cost_2021", period)
        cost_22 = tax_unit("alt_energy_device_cost_2022", period)
        portion_deductible = p.alt_energy_device_deduction[year]

        # Multiply percentage by device and sum
        deduction_2019 = cost_19 * portion_deductible
        deduction_2020 = cost_20 * portion_deductible
        deduction_2021 = cost_21 * portion_deductible
        deduction_2022 = cost_22 * portion_deductible
        deduction_total = (
            deduction_2019 + deduction_2020 + deduction_2021 + deduction_2022
        )
        return min(deduction_total, limit)
