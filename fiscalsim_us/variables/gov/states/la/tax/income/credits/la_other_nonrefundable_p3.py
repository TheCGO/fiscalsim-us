from fiscalsim_us.model_api import *


class la_other_nonrefundable_p3(Variable):
    """
    Louisiana nonrefundable priority 3 credits not yet implimented as separate variables
    Form IT-540 line 20
    These include the following credits with codes:
    202 – Organ Donation
    208 – Previously Unemployed
    221 – Owner of Accessible and Barrier-free Home –
    224 – New Jobs Credit
    228 – Eligible Re-entrants –
    236 – Apprenticeship (2007)
    251 – Motion Picture Investment
    252 – Research and Development
    253 – Historic Structures
    254 – Digital Interactive Media
    257 – Capital Company
    258 – LA Community Development Financial Institution (LCDFI)
    259 – New Markets
    261 – Motion Picture Infrastructure
    262 – Angel Investor
    300 – Biomed/University Research
    305 – Tax Equalization
    310 – Manufacturing Establishment
    412 – Refund by Utilities
    424 – Donation to School Tuition Organization
    454 – QMC Music Job Creation Credit
    457 – Neighborhood Assistance
    458 – Research and Development
    459 – Ports of Louisiana Import Export Cargo
    460 – LA Import
    461 – LA Work Opportunity
    462 – Youth Jobs
    463 – Apprenticeship (2022)
    464 – Donation to Qualified Foster Care Charitable Organization
    500 – Inventory Tax Credit Carried Forward and ITEP
    502 – Ad Valorem Natural Gas Credit Carried Forward
    504 – Atchafalaya Trace
    506 – Cane River Heritage
    508 – Ports of Louisiana Investor
    510 – Enterprise Zone
    550 – Recycling Credit
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana nonrefundable priority 3 income tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
