from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A premium version of the Taxi class."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise subclass SilverServiceTaxi, inheriting from Taxi parent."""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness * self.price_per_km)
        self.flagfall_count = 0

    def start_fare(self):
        """Start recording fare cost."""
        self.flagfall_count += 1

    def get_fare(self):
        """Calculate fare cost, based on current distance."""
        return (self.current_fare_distance * self.fanciness) + (self.flagfall_count * self.flagfall)