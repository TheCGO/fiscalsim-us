from fiscalsim_us.model_api import *


class ga_nol_carryover_addition(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia addition to incone for net operating loss carryover deducted on federal return"
    unit = USD
    definition_period = YEAR
    reference = "https://houpl.org/wp-content/uploads/2023/01/2022-IT-511_Individual_Income_Tax_-Booklet-compressed.pdf#page=34"
    defined_for = StateCode.GA
