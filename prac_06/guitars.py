"""CP1404 Practical 06: Classes - Do-from-scratch exercises."""
from guitar import Guitar
MINIMUM_VALUE = 0


def main():
    """Store all of input guitars in a list, then print their details."""
    print("My guitars!")


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
