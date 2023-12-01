from fiscalsim_us.model_api import *


class ga_series100_nonrefundable_credits(Variable):
    """
    Georgia nonrefundable Series 100 tax credits. Line 20 Form 500
    These credits are claimed using the Form 500 Schedule 2.
    A tax unit may only claim series 100 tex credits if they
    file online.
    These credits include the following with the codes:
    102 - Employer’s Credit for Approved Employee Retraining
    103 - Employer’s Jobs Tax Credit
    104 - Employer’s Credit for Purchasing Child Care
    Property
    105 - Employer’s Credit for Providing or Sponsoring
    Child Care for Employees
    106 - Manufacturer’s Investment Tax Credit
    107 - Optional Investment Tax Credit
    108 - Qualified Transportation Credit (only carryover
    can be used)
    109 - Low Income Housing Credit
    111 - Business Enterprise Vehicle Credit
    112 - Research Tax Credit
    113 - Headquarters Tax Credit
    114 - Port Activity Tax Credit
    115 - Bank Tax Credit
    116 - Low Emission Vehicle Credit (only carryover can
    be used)
    117 - Zero Emission Vehicle Credit (only carryover can
    be used)
    118 - New Facilities Job Credit
    119 - Electric Vehicle Charger Credit
    120 - New Manufacturing Facilities Property Credit
    121 - Historic Rehabilitation Credit for Historic Homes
    122 - Film Tax Credit (Use code 133 if the credit is for a
    Qualified Interactive Entertainment Production Company)
    124 - Land Conservation Credit
    125 - Qualified Education Expense Credit
    126 - Seed-Capital Fund Credit
    128 - Wood Residual Credit
    130 - Quality Jobs Tax Credit
    131 - Alternate Port Activity Tax Credit
    132 - Qualified Investor Tax Credit
    133 - Film Tax Credit for a Qualified Interactive Entainment Production Company
    135 - Historic Rehabilitation Tax Credit for any Other Certified Structures
    136 - Qualified Rurual Hospital Organization Expense Tax Credit
    138 - Postproduction Film Tax Credit
    139 - Small Postproduction Film Tax Credit
    140 - Qualified Education Donation Tax Credit
    141 - Musical Tax Credit
    142 - Rural Zone Tax Credit
    143 - Agribusiness and Rural Jobs Tax Credit
    144 - Post- Consumer Waste Materials Tax Credit
    145 - Timber Tax Credit
    146 - Railroad Track Maintenance Tax Credit
    147 - Personal Protective Equipment Manufacturer Jobs Tax Credit
    148 - Life Sciences Manufacturing Job Tax Credit
    149 - Historic Rehabilitation Tax Credit for Historic Homes and other Certified Structure
    """

    value_type = float
    entity = TaxUnit
    label = "Georgia series 100 nonrefundable credits"
    reference = "https://dor.georgia.gov/it-511-individual-income-tax-booklet"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.GA

    # These are really hard to find the specifics since you need to file online
    # to get them.
