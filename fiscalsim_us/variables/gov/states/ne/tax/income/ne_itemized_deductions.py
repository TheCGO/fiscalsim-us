from fiscalsim_us.model_api import *


class ne_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "NE itemized deductions"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.nebraska.gov/files/doc/tax-forms/2021/f_1040n_booklet.pdf"
        "https://revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_5.pdf"
    )
    defined_for = StateCode.NE

    def formula(tax_unit, period, parameters):
        # 2021 Form 1040N instructions say this:
        #   If you use the standard deduction on the federal return,
        #   you must use the Nebraska standard deduction on the
        #   Nebraska return.  All taxpayers that claimed itemized
        #   deductions on their federal return are allowed the larger
        #   of the Nebraska standard deduction or federal itemized
        #   deductions, minus state and local income taxes claimed on
        #   Federal Schedule A.
        us_itemizing = tax_unit("tax_unit_itemizes", period)
        # calculate US itemized deductions less state non-property taxes
        p = parameters(period).gov.irs.deductions
        items = [
            deduction
            for deduction in p.itemized_deductions
            if deduction not in ["salt_deduction"]
        ]
        us_itm_deds_less_salt = add(tax_unit, period, items)
        filing_status = tax_unit("filing_status", period)
        capped_property_taxes = min_(
            add(tax_unit, period, ["real_estate_taxes"]),
            p.itemized.salt_and_real_estate.cap[filing_status],
        )
        ne_itm_deds = us_itm_deds_less_salt + capped_property_taxes
        return us_itemizing * ne_itm_deds
