from fiscalsim_us.model_api import *


class ar_income_adjustments(Variable):
    """Line 24 of Form AR1000F
    Adjustments include:
        Border city/Texarkana exemption
        Tuition Savings Program
        Payments to IRA
        Payments to MSA
        Payments to HSA
        Deduction for interest paid on student loans
        Contributions to Intergenerational Trust
        Moving expenses
        Self-employed health insurance deduction
        KEOGH, Self-employed SEP and Simple Plans
        Forfeited interest penalty for premature withdrawal
        Alimony/Separate Maintenance Paid
        Support for permanently disabled individual
        Organ Donor Deduction
        Military Reserve Expenses
        Reforestation Deduction
        Teachers Qualified Classroom Investment Expense
        Achieving A Better Life Experience Program"""

    value_type = float
    entity = TaxUnit
    label = "Arkansas adjustments to total income to calculate AR AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000ADJ_AdjustmentsSchedule.pdf"
        "https://law.justia.com/codes/arkansas/2019/title-26/subtitle-5/chapter-51/subchapter-4/section-26-51-403/"
    )
    defined_for = StateCode.AR
