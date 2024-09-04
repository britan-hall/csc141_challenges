# Britan Hall
# Date: 9/4/2024
# This is assignment takes basic user input into and 'f' string and prints out a sentence.

print("To generate your introduction, I will need some information from you...")

name = input('What is your first name? ')
age = input('How old are you? ')
major = input('What is your major? ')

print(f'Hello, my name is {name.title()} and I am {age} years old! At Albright College, I study {major.title()}.')