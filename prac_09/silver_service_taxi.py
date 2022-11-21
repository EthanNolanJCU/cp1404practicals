"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""
from prac_09.taxi import Taxi

flagfall = 4.5


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.flagfall = flagfall
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + flagfall


