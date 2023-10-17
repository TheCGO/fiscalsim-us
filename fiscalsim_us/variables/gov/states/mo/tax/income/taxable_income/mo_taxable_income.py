from fiscalsim_us.model_api import *


class mo_taxable_income(Variable):
    value_type = float
    entity = Person
    label = "Missouri AGI minus deductions"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.mo.gov/forms/MO-A_2021.pdf"
        "https://dor.mo.gov/forms/MO-1040%20Instructions_2021.pdf#page=8"
        "https://dor.mo.gov/forms/MO-1040%20Instructions_2022.pdf#page=8"
        "https://www.revisor.mo.gov/main/OneSection.aspx?section=143.111&bid=7201&hl="
    )
    defined_for = StateCode.MO

    def formula(person, period, parameters):
        # calculate tax unit MO AGI
        tax_unit = person.tax_unit
        mo_agi = person("mo_adjusted_gross_income", period)
        unit_mo_agi = tax_unit.sum(mo_agi)

        # calculate sum of all tax unit MO deductions
        #   2021 and 2022 Form MO-1040 instructions on page 8 say:
        #     If you claimed the standard deduction on your federal return,
        #     enter the standard deduction amount for your filing status.
        #     The amounts are listed on Form MO-1040, Line 14.
        #     If you itemized on your federal return, you may want to itemize
        #     on your Missouri return or take the standard deduction, whichever
        #     results in a higher deduction.
        federal_itemizer = tax_unit("tax_unit_itemizes", period)
        itmded = tax_unit("mo_itemized_deductions", period)
        stdded = tax_unit("standard_deduction", period)  # same as federal
        mo_deduction = where(federal_itemizer, max_(itmded, stdded), stdded)
        unit_mo_deductions = (
            mo_deduction
            + tax_unit("mo_federal_income_tax_deduction", period)
            + tax_unit("mo_pension_and_ss_or_ssd_deduction", period)
        )
        # Note: There would also be a personal and/or dependent exemptions
        # as part of this formula, but they are legally based on eligibility
        # for the federal versions of those exemptions, both of which are
        # suspended through 2025 federally.

        # calculate taxable income for tax unit
        unit_taxinc = max_(0, unit_mo_agi - unit_mo_deductions)

        # allocate tax unit taxable income by each individual's share of
        # unit AGI (use a mask rather than where to avoid a divide-by-zero
        # warning with default share value being zero)
        ind_agi_share = np.zeros_like(unit_mo_agi)
        mask = unit_mo_agi > 0
        ind_agi_share[mask] = mo_agi[mask] / unit_mo_agi[mask]

        return ind_agi_share * unit_taxinc
