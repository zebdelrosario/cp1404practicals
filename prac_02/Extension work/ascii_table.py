"""
Program that converts ASCII characters to alphabetical and vice versa.
"""

LOWER = 33
UPPER = 127

alpha_character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(alpha_character, ord(alpha_character)))
ascii_character = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while ascii_character < LOWER or ascii_character > UPPER:
    print("Invalid number, please enter a number between {} and {}!".format(LOWER, UPPER))
    ascii_character = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(ascii_character, chr(ascii_character)))

columns = int(input("Enter number of columns: \n>"))
count = 0
for i in range(LOWER, UPPER):
    count += 1
    result = "{:>3}{:>2}".format(i, chr(i))  # string formatting to print corresponding char e.g.: "46 ."
    if count % columns != 0:
        print(result, end="\t")
    else:
        print(result)
