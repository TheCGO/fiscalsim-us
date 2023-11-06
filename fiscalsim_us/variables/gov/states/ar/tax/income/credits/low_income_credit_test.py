def calculate_credit_amount(tax_rate, adjustment, credit_rate, min_income, phaseout_rate, taxable_income, deduction):
    # Calculate the tax liability on min_income
    tax_liability = ((min_income-deduction) * tax_rate) - adjustment

    # Calculate the credit amount
    credit_amount = tax_liability * credit_rate
    print(credit_amount)

    # Calculate the phaseout reduction for each $100 over min_income
    excess_income = taxable_income - min_income
    phaseout_reduction = excess_income // 100 * phaseout_rate

    # Reduce the credit amount based on the phaseout reduction
    credit_amount -= phaseout_reduction

    # Ensure credit_amount does not go below 0
    if credit_amount < 0:
        credit_amount = 0

    return credit_amount

# Example usage:
tax_rate = 0.03
adjustment = 204.97
credit_rate = 0.8
min_income = 13450
phaseout_rate = 4
taxable_income = 13550
deduction = 2270

# test = (((min_income-2270) * tax_rate) - adjustment) * credit_rate
# print('test: ', test)

credit_amount = round(calculate_credit_amount(tax_rate, adjustment, credit_rate, min_income, phaseout_rate, taxable_income, deduction),0)
print(f"Credit Amount: ${credit_amount:.2f}")