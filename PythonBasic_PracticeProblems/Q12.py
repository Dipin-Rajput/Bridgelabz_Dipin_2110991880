# 12) Calculate income tax: Calculate income tax for the given income by adhering to specific rules.

# Specific rules:

# There is no tax for individuals with an income of up to ₹3 lakhs.
# For individuals with an income between ₹3 lakhs and ₹6, the tax rate is 5%.
# For individuals with an income between ₹6 lakhs and ₹9 lakhs, the tax rate is 10%.
# For individuals with an income between ₹9 lakhs and ₹12 lakhs, the tax rate is 15%.
# For individuals with an income between ₹12 lakhs and ₹15 lakhs, the tax rate is 20%.
# For individuals with an income above ₹15 lakhs, the tax rate is 30%.

income = int(input("Enter your income: "))
standard_deduction = 50000
taxable_amount = income - standard_deduction

if(taxable_amount <= 300000):
    print("No tax for you")
elif(taxable_amount >= 300001 and income <= 600000):
    income_tax = taxable_amount * (5/100)
    print("Your income tax amount after standard_deduction is:", income_tax)
elif(taxable_amount >= 600001 and income <= 900000):
    income_tax = taxable_amount * (10/100)
    print("Your income tax amount after standard_deduction is:", income_tax)
elif(taxable_amount>= 900001 and income <= 1200000):
    income_tax = taxable_amount * (15/100)
    print("Your income tax amount after standard_deduction is:", income_tax)
elif(taxable_amount >= 1200001 and income <= 1500000):
    income_tax = taxable_amount * (20/100)
    print("Your income tax amount after standard_deduction is:", income_tax)
else:
    income_tax = taxable_amount * (30/100)
    print("Your income tax amount after standard_deduction is:", income_tax)