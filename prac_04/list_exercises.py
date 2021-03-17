"""
A program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
Then, output various interesting things.
"""
NUMBER_OF_PROMPTS = 5


def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    for i in range(NUMBER_OF_PROMPTS):
        number = int(input("Number: "))
        numbers.append(number)
    display_various_things(numbers)
    username = input("Username: ").lower()
    usernames = [c.lower() for c in usernames]  # convert all elements in usernames to .lower
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def display_various_things(numbers):
    """Display a variety of things using list of data."""
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    numbers_average = sum(numbers) / len(numbers)
    print("The first number is {}".format(first_number))
    print("The last number is {}".format(last_number))
    print("The smallest number is {}".format(smallest_number))
    print("The largest number is {}".format(largest_number))
    print("The average of the numbers is {}".format(numbers_average))


main()
