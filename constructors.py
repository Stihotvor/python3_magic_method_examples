class Vessel:
    def __new__(cls, *args, **kwargs):
        """
        Creating new class instance
        :param args:
        :param kwargs:
        """
        return object.__new__(cls)

    def __init__(self, name: str):
        """
        Initializing class instance with vessel name
        :param name:
        """
        self.name = name
        self.fuel = 0.0

        # list of dicts with passenger attributes
        self.passengers = []

    def __del__(self):
        """
        Destructing class instance. Used for safe instance destruction
        :return:
        """
        self.pump_out_fuel()
        self.discharge_passengers()

    # Vessel methods
    def pump_in_fuel(self, quantity: float):
        self.fuel += quantity

    def pump_out_fuel(self):
        self.fuel = 0.0

    def discharge_passengers(self):
        self.passengers = []


if __name__ == '__main__':
    # Runtime tests will be here
    vsl_1 = Vessel(name='Calypso')

