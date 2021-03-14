"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print("Your result is: {}".format(result))
    result = determine_result(random.randint(0, 100))
    print("Your random result is: {}".format(result))


def determine_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()
