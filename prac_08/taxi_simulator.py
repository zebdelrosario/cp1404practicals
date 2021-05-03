"""Practical 08 - Taxi Simulator program.
Choose a taxi from a provided list and receive a bill corresponding to distance driven."""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
import random
MENU_CHOICES = ["q", "c", "d"]
AMOUNT_OF_TAXIS = 3


def main():
    """Taxi simulator: choose from a list of Taxis and drive."""
    print("Let's drive!")
    taxis = generate_taxis(AMOUNT_OF_TAXIS)
    menu_choice = get_valid_choice(">>> ")
    while menu_choice != MENU_CHOICES[0]:
        if menu_choice == MENU_CHOICES[1]:  # Choose taxi
            pass
        elif menu_choice == MENU_CHOICES[2]:  # Drive taxi
            pass


def get_valid_choice(prompt):
    """Prompt user until valid choice is selected."""
    user_choice = input(prompt).lower()
    while user_choice not in MENU_CHOICES:
        print("Please select a valid menu option!")
    return user_choice


def generate_taxis(amount_of_cars):
    """Generate a random list of taxis using a list of car models."""
    taxis = []
    car_models = [Taxi("Ford Mondeo", 100), Taxi("Holden Caprice", 100), Taxi("Toyota HiAce", 100),
                  SilverServiceTaxi("Ford Falcon G6", 100, 2), Taxi("Toyota Tarago", 100)]
    for i in range(amount_of_cars):
        car_model_index = random.randint(0, len(car_models)-1)
        taxi = car_models[car_model_index]
        while taxi in taxis:
            car_model_index = random.randint(0, len(car_models)-1)
            taxi = car_models[car_model_index]
        taxis.append(taxi)
    return taxis


main()
