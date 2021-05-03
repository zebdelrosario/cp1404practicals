from prac_08.car import Car
from prac_08.taxi import Taxi

# Print the taxi's details and the current fare
new_taxi = Taxi("Prius 1", 100)
new_taxi.drive(40)
print(f"""Taxi's details:
{"Name:":>10} {new_taxi.name}
Fare cost: $ {new_taxi.get_fare():>6.2f}\n""")


# Restart the meter (start a new fare) and then drive the car 100km
# Print the details and the current fare
new_taxi.start_fare()
new_taxi.drive(100)
print(f"""Taxi's details:
{"Name:":>10} {new_taxi.name}
Fare cost: $ {new_taxi.get_fare():>6.2f}""")
