"""CP1404 Practical 06: Classes - Do-from-scratch exercises."""
from guitar import Guitar
MINIMUM_VALUE = 0


def main():
    """Store all of input guitars in a list, then print their details."""
    guitars = []
    print("My guitars!")
    guitar_name = get_valid_string("Name: ")
    while guitar_name != "":
        guitar_year = get_valid_integer("Year: ")
        guitar_cost = get_valid_float("Cost: ")
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        guitar_name = get_valid_string("Name: ")
    display_all_guitars(guitars)


def display_all_guitars(guitars):
    """Display all guitars in a list in a neat format."""
    for i, guitar in enumerate(guitars):
        print_format = f"Guitar {i+1}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}"
        if not guitar.is_vintage():
            print(print_format)
        else:
            print(print_format + " (vintage)")


def get_valid_string(prompt):
    """Prompt user until a valid string is entered."""
    is_valid_string = False
    while not is_valid_string:
        try:
            string = str(input(prompt))
            return string
        except ValueError:
            print("Value Error, please enter a STRING!")


def get_valid_float(prompt):
    """Prompt user until a valid float is entered."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input(prompt))
            if number < MINIMUM_VALUE:
                print(f"Number is too small! Enter a float > {MINIMUM_VALUE}!")
            else:
                return number
        except ValueError:
            print(f"Value Error; enter a valid float that's >{MINIMUM_VALUE}!")


def get_valid_integer(prompt):
    """Prompt user until a valid integer is entered."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number < MINIMUM_VALUE:
                print(f"Number is too small! Enter an integer > {MINIMUM_VALUE}!")
            else:
                return number
        except ValueError:
            print(f"Value Error; enter a valid integer that's >{MINIMUM_VALUE}!")


main()
