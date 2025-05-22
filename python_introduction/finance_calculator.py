# Python script named finance_calculator.py. 
# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.


# User Input for Financial Details
monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculate Monthly Savings
monthly_savings = monthly_income - total_monthly_expenses

# Project Annual Savings
annual_interest_rate = 0.05
month_in_a_year = 12
projected_savings = (monthly_savings * 12 + (monthly_savings * month_in_a_year * annual_interest_rate))

# Output result
print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)
