from fiscalsim_us.model_api import *


class mn_other_subtractions(Variable):
    """
    Line 7 of Minnesota 2022 Individual Income Tax return from M1. These
    subtractions from income include the following categories which are
    not included as other variables directly.
    * Education expense paid for qulaifying children in grades K-12
    * Qualifying contributions to education savings plan
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

    # if any get implimented as vars, delete from list
