from random import randint

class Die:
    """A Class represeenting a single Dice"""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
