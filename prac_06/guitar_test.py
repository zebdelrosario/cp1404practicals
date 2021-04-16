"""CP1404 Practical 06: Classes - Do-from-scratch exercises."""
from guitar import Guitar
from datetime import datetime


def main():
    """Test guitar.py module for errors."""
    guitar_one = Guitar("Gibson L-5 CE", 1922, 16035.40)  # Expected: 99, True
    guitar_two = Guitar("Martin OM-45", 1930, 265000.00)  # Expected: 91, True
    guitar_three = Guitar("Jazzmaster Squier", 1990, 399.00)  # Expected: 31, False
    print(f"{guitar_one.name} get_age() - Expected 99. Got {guitar_one.get_age()}")
    print(f"{guitar_two.name} get_age() - Expected 91. Got {guitar_two.get_age()}")
    print(f"{guitar_three.name} get_age() - Expected 31. Got {guitar_three.get_age()}")
    print(f"{guitar_one.name} is_vintage() - Expected True. Got {guitar_one.is_vintage()}")
    print(f"{guitar_two.name} is_vintage() - Expected True. Got {guitar_two.is_vintage()}")
    print(f"{guitar_three.name} is_vintage() - Expected False. Got {guitar_three.is_vintage()}")


main()
