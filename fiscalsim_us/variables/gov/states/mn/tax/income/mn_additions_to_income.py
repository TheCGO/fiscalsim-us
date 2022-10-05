from fiscalsim_us.model_api import *


class mn_additions_to_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN additions to Federal Ajusted Gross Income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.state.mn.us/sites/default/files/2021-12/m1m_21.pdf"
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        #interest_from_muni_bonds_of_other_state = ?
        #fed_tax_exempt_dividends_of_muni_bonds_in_mutual_fund = ?
        #fed_expenses_deducted_not_taxed_mn = ?
        #cap_gains_of_lump_sum_distribution = ?
        #K-12_tuition_from_higher_ed_saving_acct = ?
        #line_35_schedule_M1NC = ?

        return 0 # acually return the sum of the things above
