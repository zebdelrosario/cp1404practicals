"""Practical 08 - Taxi Simulator program.
Choose a taxi from a provided list and receive a bill corresponding to distance driven."""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU_CHOICES = ["q", "c", "d"]


def main():
    """Taxi simulator: choose from a list of Taxis and drive."""
    menu_choice = get_valid_choice(">>>")


def get_valid_choice(prompt):
    """Prompt user until valid choice is selected."""
    user_choice = input(prompt).lower()
    while not user_choice in MENU_CHOICES:
        print("Please select a valid menu option!")
    return user_choice

main()
