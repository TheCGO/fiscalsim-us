from fiscalsim_us.model_api import *


class mn_other_subtractions_from_income(Variable):
    """
    Line 7 of Minnesota 2022 Individual Income Tax return from M1. These
    subtractions from income include the following categories and are listed in
    Schedule M1M
    * Qulaifying charitable distributions if not filing itemized deductions
    * Social Security benefit subtraction
    * Education expense paid for qulaifying children in grades K-12
    * Net interest or mutual fund distributions from US bonds
    * Qualifying contributions to education savings plan
    * Subtraction for persons 65+ or permanently dissabled
    * Railroad retirement benefits
    * Reservation income for American Indians
    * Federal activate duty military pay while Minnesota resident
    * Organ donor subtraction
    * Volunteer mileage reimbursment subtraction
    * Subtraction for miliary pensions and retirement
    * Payment from Minnesota Frontline Worker Pay Program
    """

    value_type = float
    entity = TaxUnit
    label = "MN other subtrations from income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
