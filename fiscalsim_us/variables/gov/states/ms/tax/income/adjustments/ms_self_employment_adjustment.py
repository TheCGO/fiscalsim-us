from fiscalsim_us.model_api import *


class ms_self_employment_adjustment(Variable):
    value_type = float
    entity = TaxUnit
    label = "Mississippi self employment adjustment"
    unit = USD
    definition_period = YEAR
    reference = [
        "https://www.dor.ms.gov/sites/default/files/Forms/Individual/80100221.pdf#page=13",  # Line 61
        "https://law.justia.com/codes/mississippi/2020/title-27/chapter-7/article-1/section-27-7-18/",  # 6(c)
    ]
    defined_for = StateCode.MS

    def formula(tax_unit, period, parameters):
        self_employment_tax = add(tax_unit, period, ["self_employment_tax"])
        p = parameters(
            period
        ).gov.states.ms.tax.income.adjustments.self_employment
        return self_employment_tax * p.rate
