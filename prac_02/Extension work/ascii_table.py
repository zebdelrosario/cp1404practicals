"""
Program that converts ASCII characters to alphabetical and vice versa.
"""

LOWER = 33
UPPER = 127
#
# alpha_character = input("Enter a character: ")
# print("The ASCII code for {} is {}".format(alpha_character, ord(alpha_character)))
# ascii_character = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
# while ascii_character < LOWER or ascii_character > UPPER:
#     print("Invalid number, please enter a number between {} and {}!".format(LOWER, UPPER))
#     ascii_character = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
# print("The character for {} is {}".format(ascii_character, chr(ascii_character)))


for i in range(LOWER, UPPER):
    print("{:>3}{:>2}".format(i, chr(i)))
