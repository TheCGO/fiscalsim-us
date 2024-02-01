from fiscalsim_us.model_api import *

class ar_capital_gains(Variable):
    
    value_type = float
    entity = TaxUnit
    label = "Arkansas taxable capital gains"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000D_CapitalGains.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):

        filing_status = tax_unit('filing_status', period)
        
        p = parameters(period).gov.states.ar.tax.income.capital_gains

        max_taxable_gain = p.max_taxable_capital_gain

        ar_lt_taxable_pct = p.long_term_cap_gain_taxable_pct

        cap_loss_cap = p.capital_loss_cap

        lt_gains = tax_unit("long_term_capital_gains", period)

        non_d_gains = tax_unit("non_sch_d_capital_gains", period)

        lt_dep_adjustment = tax_unit('ar_lt_dep_adjustment', period)

        ar_lt_gain = lt_gains + non_d_gains + lt_dep_adjustment

        st_gain = ("short_term_capital_gains", period)

        st_dep_adjustment = tax_unit('ar_st_dep_adjustment', period)

        ar_st_gain = st_gain + st_dep_adjustment

        # if there are short term losses, but net gains are positive, net gain should equal the min of max_taxable_gain or the difference between the long term gain and short term loss. 
        # if there short term losses, and net losses, net gain should equal the total loss
        # if there are short term gains, those are handled later.

        ar_net_lt_gain = where(
            ar_st_gain < 0, where(
                ar_lt_gain - ar_st_gain >= 0, min(max_taxable_gain, ar_lt_gain - ar_st_gain), ar_lt_gain + ar_st_gain
            ), 
            min(ar_lt_gain, max_taxable_gain)
        )

        ar_taxable_amount = where(
            ar_net_lt_gain > 0, ar_net_lt_gain * ar_lt_taxable_pct, ar_net_lt_gain
        )

        total_taxable = where(
            ar_st_gain >=0, ar_st_gain + ar_taxable_amount,
            ar_taxable_amount
        )

        total_taxable = where(
            total_taxable <= 0, min(total_taxable, cap_loss_cap[filing_status])
        )

        return total_taxable





        