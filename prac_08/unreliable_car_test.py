import random
from prac_08.car import Car


class UnreliableCar(Car):
    """A Car class that has a random chance of failing."""
    reliability_chance = float(random.randint(0, 100))

    def __init__(self, name, fuel, reliability=reliability_chance):
        super().__init__(name, fuel)
        self.reliability = reliability

    def attempt_drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            distance_driven = self.drive(distance)
            print(f"Distance: {distance_driven}km")
        else:
            print("Distance: 0km")


bad_car = UnreliableCar("Bad car", 100)
bad_car.attempt_drive(50)
