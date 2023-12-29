#This program calculates:
#1. The amount of interest a customer earns on their investment.
### Customer enters the initial amount of investment(principal),
### the interest rate(percentage), the number of years to invest,
### and the type of interest (simple or compound)
### Program outputs the amount customer earns after specified years.
#2. The amount to pay on a home loan
### Customer enters present value of house, interest rate(percentage)
### and the number of months they prefer to repy the loan
### Program outputs the amount to repy each month.

import math

print("\n********************************************")
print("Welcome to investment and bond calculator ")
print("********************************************")

#investment or bond
calculation_type = ""

#Investment variable initialisations
investment_principal = 0.0
investment_rate = 0.0
investment_years = 1
investment_amount = 0.0
investment_type = "" #simple or compound
is_investment = False #to check if investment option is selected

#Bond variable initialisations
bond_value = 0.0
bond_interest_rate = 0.0
bond_repayment_months = 1
bond_monthly_repayment_amount = 0.0
is_bond = False #to check if bond option is selected

#boolean to check validity of entered values
valid_values = True

print("-------------------------------------------------------------------------------------")
print("\ninvestment - to calculate the amount of interest you will earn on your investment.")
print("\nbond - to calculate the amount you'll have to pay on a home loan.")
print("-------------------------------------------------------------------------------------")
print()
calculation = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
calculation_option = calculation.lower()

if calculation_option == "investment":
   is_investment = True
elif calculation_option == "bond":
   is_bond = True
else:
   print("Invalid input")
   
if is_investment:
   invest_type = input("\nEnter investment type (simple or compound): ")
   investment_type = invest_type.lower()

   investment_principal = float(input("\nEnter the amount of money you want to deposit: £"))
   investment_rate = float(input("\nEnter the interest rate (e.g. 2 for 2%): " )) 
   investment_years = int(input("\nEnter the number of years you want to invest your money for: "))

   #checking validity of entered values
   if investment_principal <= 0 or investment_rate <= 0 or investment_years < 1:
      valid_values = False
     
   if investment_type == "compound" and valid_values == True:  
      #calculate the amount of investment with compound interest 
      investment_amount = investment_principal*(1 + investment_rate/100)**investment_years
      print()
      print("Outcome")
      print("*************************************************************")
      print(f"Investment type: {investment_type}")
      print(f"Amount invested: £{round(investment_principal,2)}") #rounding value to 2 decimal places
      print(f"Interest rate {investment_rate}%")
      print(f"Number of years invested: {investment_years} years")
      print(f"Current balance: £{round(investment_amount,2)}")
      print("*************************************************************")
   
   elif investment_type == "simple" and valid_values == True:  
      #calculate the amount of investment with simple interest 
      investment_amount = investment_principal*(1 + (investment_rate/100)*investment_years)
      print()
      print("Outcome")
      print("*************************************************************")
      print(f"Investment type: {investment_type}") 
      print(f"Amount invested: £{round(investment_principal,2)}")
      print(f"Interest rate: {investment_rate}%")
      print(f"Number of years invested: {investment_years} years")
      print(f"Current balance: £{round(investment_amount,2)}")
      print("*************************************************************")

   else:
      print("\nError! Either value/s entered is/are invalid or the type of investment entered may have been misspelt.")

elif is_bond:
      bond_value = float(input("\nEnter the value of the house: £"))
      bond_interest_rate = float(input("\nEnter the bond's interest rate (e.g. 2 for 2%): " )) 
      bond_repayment_months = int(input("\nEnter the number of months you want to repay the bond: "))

      if bond_value <= 0 or bond_interest_rate <= 0 or bond_repayment_months < 1:
         valid_values = False
         print("\nOne or more of your input value(s) is/are invalid!")

      if valid_values:
         #monthly interest rate - annual rate divided by 100 and then divide by 12 yields monthly rate
         i = ((bond_interest_rate/100)/12 )
         p = bond_value
         n = bond_repayment_months
         bond_monthly_repayment_amount = (i * p)/(1 - (1 + i)**(-n))
         print()
         print("Outcome")
         print("*************************************************************")
         print(f"Present value of house: £{round(bond_value,2)}")
         print(f"Bond interest rate {bond_interest_rate}%")
         print(f"Number of repayment months: {bond_repayment_months} months")
         print(f"Amount to repay each month: £{round(bond_monthly_repayment_amount,2)}")
         print("*************************************************************")


