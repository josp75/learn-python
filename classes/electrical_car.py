from classes.car import Car


class ElectricalCar(Car):
    def __init__(self, make, model, year, name):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.name = name
