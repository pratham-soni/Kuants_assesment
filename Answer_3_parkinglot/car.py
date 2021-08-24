from vehicle import Vehicle


class Car(Vehicle):
    """
    This is class which represents details of a car.
    """

    def __init__(self, registration_no=None, colour=None):
        self._registration_no = registration_no
        self._colour = colour

    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = value
