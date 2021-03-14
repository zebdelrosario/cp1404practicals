"""
Write 3 different versions of code to generate a random Boolean (True or False).
"""

import random


# Version 1
random_number = random.randint(0, 1)  # using randint
if random_number == 0:
    result_version_one = True
else:
    result_version_one = False
print(result_version_one)


# Version 2
result = random.choice((True, False))  # using random.choice
print(result)


# Version 3
random_number = random.randrange(0, 100)  # using randrange
if random_number <= 50:
    result = False
else:
    result = True
print(result)
