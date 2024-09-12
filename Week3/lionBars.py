# Britan Hall
# 9/11/2024
# This program calculates and displays the total weight of Lion Bars produced in ounces and pounds.

weight_per_bar = float(input("Enter the weight of one Lion Bar in ounces: "))
number_of_bars = int(input("Enter the number of Lion Bars made last month: "))

total_weight_ounces = weight_per_bar * number_of_bars
total_weight_pounds = int(total_weight_ounces / 16)
remaining_ounces = total_weight_ounces % 16

print()
print("Lion Bars Production Report")
print("-------------------------------")
print(f'Monthly production: {number_of_bars} @ {weight_per_bar} oz per bar.')
print(f'Total weight produce: {total_weight_ounces} oz, Which is {total_weight_pounds} lb(s), {remaining_ounces} oz.')