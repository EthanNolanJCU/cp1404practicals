from prac_09.car import Car
from random import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes the reliability of it"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with car's reliability."""
        return f"{super().__str__()}, reliability: {self.reliability}"

    def drive(self, distance):
        """Drives the car a specific distance if the car starts based upon the reliability of the car"""
        if random() * 100 < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance
