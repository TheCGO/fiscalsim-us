from fiscalsim_us.model_api import *


class az_family_income_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ Family Income Tax Credit"
    unit = USD
    documentation = (
        "AZ Family Income Tax Credit on line 50 of form 140"
    )
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR


    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        dependent = person("is_tax_unit_dependent", period)
        dep_count = tax_unit.sum(dependent)

        aged_blind = tax_unit("az_aged_blind_exemption", period)
        other = tax_unit("az_other_exemptions", period)
        parents = tax_unit("az_parents_grandparents_exemption", period)
        az_agi = tax_unit("az_agi", period)
        worksheet_1 = aged_blind + other + parents +  az_agi

        p = parameters(period).gov.states.az.tax.income.credits.family_income
        filing_status = tax_unit("filing_status", period)
        status = filing_status.possible_values

        single = p.single_seperate
        joint = p.joint
        hoh = p.head_of_household
        widow = p.head_of_household
        separate = p.single_seperate

        qualifies_limit = select(
            [
                filing_status == status.SINGLE,
                filing_status == status.JOINT,
                filing_status == status.HEAD_OF_HOUSEHOLD,
                filing_status == status.WIDOW,
                filing_status == status.SEPARATE,
            ],
            [
                single.calc(dep_count),
                joint.calc(dep_count),
                hoh.calc(dep_count),
                widow.calc(dep_count),
                separate.calc(dep_count),
            ],
        )
        
        worksheet_2_line_2 = where(
            filing_status == filing_status.possible_values.JOINT,
            2,
            1,
        )

        worksheet_2_line_3 = dep_count + worksheet_2_line_2
        worksheet_2_line_4 = worksheet_2_line_3 * 40
        worksheet_2_line_5 = where(
            filing_status == status.JOINT or
            filing_status == status.WIDOW or
            filing_status == status.HEAD_OF_HOUSEHOLD,
            240,
            120,
        )
        worksheet_2_line_6 = min_(worksheet_2_line_4, worksheet_2_line_5)    

        return  where(
            worksheet_1 <= qualifies_limit,
            worksheet_2_line_6,
            0,
        )
    