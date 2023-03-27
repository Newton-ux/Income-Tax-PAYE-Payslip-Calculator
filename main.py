monthly_income = int(input("Enter your monthly income: "))

bonus_income = int(input("Enter your bonus income: "))

nssf_pension = int(input("Enter your NSSF amount: "))

personal_pension = int(input("Enter your personal pension amount: "))

nhif_health = int(input("Enter your NHIF amount: "))

nita_employer = int(input("Enter your NITA amount: "))

mortgage_interest = int(input("Enter your mortgage interest amount: "))

insurance_premium = int(input("Enter your insurance premium amount - life/education/health with maturity period of at least 10 years: "))

csr_deduction = int(input("Enter your csr deduction amount: "))

staffwelfare_deduction = int(input("Enter your staff welfare deduction amount: "))

bankcharges_deduction = int(input("Enter your bank charges deduction amount: "))

gross_pay = monthly_income + bonus_income

if insurance_premium <= 0:
  insurance = 0
elif insurance_premium < 5000:
  insurance = insurance_premium * 0.15
else:
  insurance = 5000

# Relief is given at 15% of premiums paid up to a maximum of Kshs 60,000 per annum. For education and health, the policy should have a maturity period of at least 10 years.

if mortgage_interest <= 0:
  mortgage = 0
elif mortgage_interest < 25000:
  mortgage = mortgage_interest
else:
  mortgage = 25000

# The allowable deduction is limited to a maximum of Ksh 25,000 per month.

if personal_pension <= 0:
  pension = 0
elif personal_pension < 20000:
  pension = personal_pension
else:
  pension = 20000

# The allowable deduction is limited to a maximum of Ksh 20,000 per month.

taxable_income = gross_pay - pension - nssf_pension - mortgage

if taxable_income <= 0:
    tax = 0
elif taxable_income <= 24000:
    tax = taxable_income * 0.1
elif taxable_income <= 32332:
    tax = 2400 + (taxable_income - 24000) * 0.25
else:
    tax = 2400 + 2083.25 + (taxable_income - 32333) * 0.3

incometax_paye = tax - (2400 + 255 + insurance)

deductions = nssf_pension + nhif_health + incometax_paye + pension + csr_deduction + staffwelfare_deduction + bankcharges_deduction

print("Your gross pay is: ", "KES", gross_pay)

print("Your taxable monthly income is: ", "KES", taxable_income)

print("Your tax charge is: ", "KES", int(tax))

print("Your monthly income tax PAYE is: ", "KES", int(tax - 2400 - 255 - insurance))
# 2400 is PAYE relief and 255 is NHIF relief insurance relief capped at 5000 per month

print("The cost to your employer is: ", "KES", int(monthly_income + nssf_pension + nita_employer))

print("Your net pay is: ", "KES", int(gross_pay - deductions))

print("Your total deductions are: ", "KES", int(deductions))

print("You are paying KES", int((incometax_paye)*12), "of your income in taxes annually. This means that you work exclusively for the Government of Kenya for", int(((incometax_paye)*12)/(gross_pay - deductions)), "months every year.")
