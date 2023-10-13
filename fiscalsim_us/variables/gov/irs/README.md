# IRS

## State and local tax (SALT) Deduction

The SALT deduction previously created a circularity with some states' tax logic because itemizing federal filers can deduct current-year prepayments of state and local income tax liability (if greater than state and local sales tax liability) in the state and local tax deduction on the federal form. However, that current state and local income tax liability is simultaneously calculated and in some states requires the value of federal taxable income, which includes (subtracts) the SALT deduction. This creates a circularity in the tax logic that FiscalSim-US is not able to handle at this point.

To be clear, the tax logic correctly includes this circularity. However, our solution is to write the code in the way that most filers use the SALT deduction, excluding the case in which filers deduct current-year state and local income tax liability. We created two new variables--`prior_year_state_income_tax_paid` and `prior_year_local_income_tax_paid`--and used those variables in the calculation of `statelocal_sales_or_prior_inctax`, which in turn goes into the `salt_deduction` variable calculation. In other words, the SALT deduction calculation in FiscalSim-US only allows for deducting prior year state and local income taxes.

There is a workaround for capturing the effect of those who include their current-year paid state and local income taxes in their SALT deduction. Because the variables `prior_year_state_income_tax_paid` and `prior_year_local_income_tax_paid` are just household tax unit variables, a user can just increase those amounts to whatever level of total state and local income taxes paid go into the SALT deduction calculation.
