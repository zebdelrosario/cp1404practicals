import random

from prac_08.car import Car


class UnreliableCar(Car):
    """A Car class that has a random chance of failing."""
    reliability_chance = float(random.randint(0, 100))

    def __init__(self, name, fuel, reliability=reliability_chance):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            print(f"{self.name} failed to drive! :(")