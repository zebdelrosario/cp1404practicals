"""CP1404 Practical 06: Classes - Do-from-scratch exercises."""
from guitar import Guitar
MINIMUM_VALUE = 0


def main():
    """Store all of input guitars in a list, then print their details."""
    print("My guitars!")
    guitar_name = get_valid_string("Name: ")
    guitar_year = get_valid_number("Year: ")
    guitar_cost = float(get_valid_number("Cost: "))


def get_valid_string(prompt):
    """Prompt user until a valid string is entered."""
    is_valid_string = False
    while not is_valid_string:
        try:
            string = str(input(prompt))
            return string
        except ValueError:
            print("Value Error, please enter a STRING!")


def get_valid_number(prompt):
    """Prompt user until a valid number is entered."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number < MINIMUM_VALUE:
                print(f"Number is too small! Enter a number > {MINIMUM_VALUE}!")
            else:
                return number
        except ValueError:
            print(f"Value Error; enter a valid number that's >{MINIMUM_VALUE}!")


main()
