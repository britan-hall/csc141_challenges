# Britan Hall
# 9/12/2024
# This script prompts the user to enter a number of scores, calculates the average of those scores, and prints the result in a styled format.

print("\n" + "=" * 25)
print('Average Score Calculation')
print("=" * 25)

number_of_scores = int(input('How many scores would you like to average? '))

scores = []


for index in range(number_of_scores):
    score = float(input(f"Enter score {index + 1}: "))
    scores.append(score)

average_score = sum(scores) / len(scores)

print("\n" + "-" * 50)
print('RESULT')
print("-" * 50)
print(f'The average score is: {average_score}')
print("-" * 50)
