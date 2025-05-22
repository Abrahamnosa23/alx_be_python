# Python script that asks the user for their current age and then calculates how old they will be in 2050

# variables for calculating future age
current_age= int(input("How old are you?"))
current_year = 2023
age_increase = 2050 - current_year

# Formular for calculating future age
age = current_age + age_increase

# Below will print the age of the user in 2025
print("In 2050, you will be", age, "years old.")
