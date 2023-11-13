from fiscalsim_us.model_api import *

class ar_high_income_reduction(Variable):
    
    value_type = float
    entity = TaxUnit
    label = "Arkansas low income tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_TaxTables.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        
        full_reduction= parameters(period).gov.states.ar.tax.income.high_income_reduction.high_income_reduction_amount
        min_income = parameters(period).gov.states.ar.tax.income.rates.regular_bracket_max + 1
        phaseout_rate = parameters(period).gov.states.ar.tax.income.high_income_reduction.high_income_reduction_phaseout
        agi = tax_unit('ar_agi', period)

        def round_to_nearest_50(num):
            # Calculate the nearest multiple of 100
            nearest_multiple_of_100 = round(num / 100,0) * 100
            
            # Get the last two digits
            last_two_digits = num % 100
            
            # Determine the closest ending in "50"
            if last_two_digits <= 50:
                rounded_income = nearest_multiple_of_100 + 50
                return rounded_income
            else:
                rounded_income = nearest_multiple_of_100 - 50
                return rounded_income

        std_ded = tax_unit("ar_standard_deduction", period)
        itm_ded = tax_unit("ar_itemized_deductions", period)
        deduction = where(itm_ded > std_ded, itm_ded, std_ded)

        agi_less_ded = agi - deduction
        min_inc_less_ded = min_income - deduction

        rounded_income = round_to_nearest_50(agi_less_ded)
        rounded_min_income = round_to_nearest_50(min_inc_less_ded)

        # Calculate the phaseout reduction for each $100 over min_income
        excess_income = rounded_income - rounded_min_income
        phaseout_reduction = excess_income // 100 * phaseout_rate

        # Reduce the credit amount based on the phaseout reduction
        reduction_amount = full_reduction - phaseout_reduction

        # Ensure credit_amount does not go below 0 and that those who itemize do not take the credit
        where(reduction_amount < 0,
            reduction_amount = 0)
        
        reduction_amount = round(reduction_amount,0)
        

        return reduction_amount