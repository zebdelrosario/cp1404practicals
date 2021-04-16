"""CP1404 Practical 06: Classes - Do-from-scratch exercises."""
from datetime import datetime
CURRENT_YEAR = str(datetime.now())  # Convert object to str to allow string-slicing


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : {self.cost:2f})"

    def get_age(self):
        """Get the age of the guitar based on its production year and current date."""
        return int(CURRENT_YEAR[:4]) - self.year  # String-slice only the year

    def is_vintage(self):
        """Determine if the guitar qualifies as a vintage guitar."""
        if self.get_age() >= 50:  # Vintage age
            return True
        return False
