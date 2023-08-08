from fiscalsim_us.model_api import *


class la_other_refundable_p2(Variable):
    """
    Other Louisiana refundable priority 2 credits listed
    on Schedule F for IT-540. These credits include the
    following with codes:
    * 52F - Ad Valorem Offshore Vessels
    * 54F – Telephone Company Property
    * 54F – Telephone Company Property
    * 58F – Milk Producers
    * 59F – Technology Commercialization
    * 60F – Historic Residential
    * 62F – Musical and Theatrical Production
    * 65F – School Readiness Child Care Provider
    * 66F – School Readiness Child Care Directors and Staff
    * 67F – School Readiness Business-Supported Child Care
    * 68F – School Readiness Fees and Grants to Resource and
    Referral Agencies
    * 70F – Retention and Modernization
    * 73F – Digital Interactive Media & Software
    * 76F – Stillborn Child
    * 77F – Funeral and Burial Expense for a Pregnancy-related Death
    * 80F – Other Refundable Credit
    """

    unit = USD
    value_type = float
    entity = TaxUnit
    label = "Louisiana other refundable priority 2 income tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
