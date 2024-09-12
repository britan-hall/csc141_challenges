# Britan Hall
# 9/12/2024
# This file generates a list of every odd number from 1 to 1,000,000 and calculates the min, max, sum, length, and mean of the list.

odd_numbers = list(range(1, 1000001, 2))

list_min = min(odd_numbers)
list_max = max(odd_numbers)
list_sum = sum(odd_numbers)
list_length = len(odd_numbers)
list_mean = list_sum / list_length

print(f'The Min number is: {list_min}')
print(f'The Max number is: {list_max}')
print(f'The Sum is: {list_sum}')
print(f'The Length is: {list_length}')
print(f'The Mean is: {list_mean}')
