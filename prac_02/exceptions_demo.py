"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_denominator = False
while not valid_denominator:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator <= 0:
            print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
            print(fraction)
            valid_denominator = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished.")


# 1.
# When the user enters anything besides an integer.

# 2.
# When the user enters 0 for the denominator.

# 3.
# Yes, by forcing the user to enter a value > 0 when asking for the denominator.
