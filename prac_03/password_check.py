"""
Program that asks user for a password until a valid one is entered.
"""

MINIMUM_LENGTH = 4
MAXIMUM_LENGTH = 10

valid_password = False
while not valid_password:
    password = str(input("Enter password:\n>"))
    password_length = len(password)
    if password_length < MINIMUM_LENGTH or password_length > MAXIMUM_LENGTH:
        print("Invalid length; enter a password between {} - {} characters".format(MINIMUM_LENGTH, MAXIMUM_LENGTH))
    else:
        valid_password = True
        print("*" * password_length)