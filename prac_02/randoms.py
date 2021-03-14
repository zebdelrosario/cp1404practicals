# What did you see on line 1?
# 16, 7, 5, 10, 9

# What was the smallest number you could have seen, what was the largest?
# Smallest 5, largest 20; due to the parameters.


# What did you see on line 2?
# 9, 9, 9, 5, 3

# What was the smallest number you could have seen, what was the largest?
# Smallest 3, largest 9; again, due to parameters.

# Could line 2 have produced a 4?
# No, as the smallest possible was 3, counting up in steps of 2 causes 4 to be skipped.


# What did you see on line 3?
# 3.522585055278799, 2.6955462992006214, 5.0944080048119496, 4.078091806677675
# What was the smallest number you could have seen, what was the largest?
# Smallest 2.5, largest 5.5; parameters


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1, 100))
