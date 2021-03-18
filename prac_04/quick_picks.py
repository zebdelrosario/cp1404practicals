"""
A program that asks a user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
"""
import random

MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1
NUMBER_PER_LINE = 6


def main():
    """Program that generates sets of random numbers."""
    # quick_picks = int(input("How many quick picks?: "))
    quick_picks = 5
    for i in range(quick_picks):
        random_numbers = []  # list gets 'reset' to avoid creating a huge list
        for j in range(NUMBER_PER_LINE):
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while random_number in random_numbers:
                random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            random_numbers.append(random_number)
        random_numbers.sort()
        print(" ".join("{:2}".format(random_number) for random_number in random_numbers))


main()

