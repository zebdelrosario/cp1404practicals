from prac_08.unreliable_car import UnreliableCar

DISTANCE = 25


def main():
    """A Car, but less reliable."""
    bad_car = UnreliableCar("Crash-Test dummy", 100)
    print(f"Driving {DISTANCE}km...")
    bad_car.drive(DISTANCE)
    if bad_car.odometer > 0:
        print(f"Distance travelled: {bad_car.odometer}km")
        print(f"Current stats: {bad_car.__str__()}")


main()

