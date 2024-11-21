from fiscalsim_us.model_api import *
import numpy as np


class ar_personal_credits(Variable):
    "Line 7A - 7D, 34 of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas personal tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ar.tax.income.credits.personal
        personal_credit_amount = p.personal_credit_amount
        person = tax_unit.members
        aged = person("age", period) >= p.age_threshold
        receives_retirement_or_disability_exemption = (
            person(
                "ar_retirement_or_disability_benefits_exemption_person", period
            )
            > 0
        )
        aged_special = aged & ~receives_retirement_or_disability_exemption
        # Only head and spouse are eligible for the personal credit amounts
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        # Blind filers get an additional personal tax credit amount
        blind = person("is_blind", period)
        # Deaf filers get an additional personal tax credit amount
        deaf = person("is_deaf", period)

        # Widowed and head of household filers receive an additional credit
        # amount
        filing_status = tax_unit("filing_status", period)
        statuses = filing_status.possible_values
        widow = filing_status == statuses.SURVIVING_SPOUSE
        hoh = filing_status == statuses.HEAD_OF_HOUSEHOLD
        whoh_filing_status_eligible = widow | hoh

        personal_credit_count = tax_unit.sum(
            head_or_spouse
            * (
                1
                + aged.astype(int)
                + blind.astype(int)
                + deaf.astype(int)
                + aged_special.astype(int)
            )
        ) + whoh_filing_status_eligible.astype(int)

        personal_credit = personal_credit_count * personal_credit_amount

        dependents = tax_unit("tax_unit_dependents", period)
        dependent_credit_amount = parameters(
            period
        ).gov.states.ar.tax.income.credits.personal.dependents
        dependent_credit = dependents * dependent_credit_amount

        qual_dependents = tax_unit(
            "ar_qual_dependents", period
        )  # Probably not implemented correctly
        qual_dependent_credit_amount = parameters(
            period
        ).gov.states.ar.tax.income.credits.personal.qual_dependents
        qual_dependent_credit = qual_dependent_credit_amount * qual_dependents

        return personal_credit + dependent_credit + qual_dependent_credit
