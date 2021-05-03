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
    print("q)uit, c)hoose taxi, d)rive")
    taxis = generate_taxis(AMOUNT_OF_TAXIS)
    current_taxi = None
    current_bill = 0.00
    menu_choice = get_valid_choice(">>> ")
    while menu_choice != MENU_CHOICES[0]:
        if menu_choice == MENU_CHOICES[1]:  # Choose taxi
            display_taxis(taxis)
            taxi_choice = get_valid_number("Choose taxi: ")
            current_taxi = taxis[taxi_choice]
        elif menu_choice == MENU_CHOICES[2]:  # Drive taxi
            current_bill += drive_taxi(current_taxi)
        print(f"Bill to date: ${current_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = get_valid_choice(">>> ")


def drive_taxi(current_taxi):
    """Drive the taxi and add cost to total bill."""
    distance_to_drive = int(input("Drive how far? "))
    current_taxi.drive(distance_to_drive)
    fare_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} cost you ${current_taxi.get_fare():.2f}")
    return fare_cost


def display_taxis(taxis):
    """Display all current available Taxis."""
    print("Taxis available:")
    i = 0
    for taxi in taxis:
        print(f"{i} - {taxi.__str__()}")
        i += 1


def get_valid_number(prompt):
    """Prompt user until a valid number is entered."""
    user_choice = int(input(prompt))
    # choice must be in range 0 - AMOUNT OF TAXIS
    while user_choice > (AMOUNT_OF_TAXIS - 1) or user_choice < 0:
        print("Error; enter a valid number!")
        user_choice = int(input(prompt))
    return user_choice


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
