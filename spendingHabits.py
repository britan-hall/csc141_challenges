# Britan Hall
# Date: 9/4/2024
# This is the second CSC 141 challenge assignment. 

PA_TAX = 0.06
PRICE_OF_MEAL = 12.49
DAYS_OF_WEEK = 5

tax_per_meal = PRICE_OF_MEAL * PA_TAX
meal_no_tax = PRICE_OF_MEAL * DAYS_OF_WEEK
total_per_week = (PRICE_OF_MEAL + (PRICE_OF_MEAL * PA_TAX)) * DAYS_OF_WEEK

print()
print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax per meal: {tax_per_meal}")
print(f"Total without tax: {meal_no_tax}")
print(f"Total with tax: {total_per_week}")
print("-------------------------")
print()