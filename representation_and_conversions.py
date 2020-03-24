class Vessel:
    def __init__(self, name: str):
        """
        Initializing class instance with vessel name
        :param name:
        """
        self.name = name
        self.fuel = 0.0

        # list of dicts with passenger attributes
        self.passengers = []

    def __repr__(self):
        """
        Instance representation
        :return:
        """
        return f'< Vessel "{self.name}">'

    def __str__(self):
        """
        String representation of the class instance
        :return:
        """
        return str(self.name)

    def __int__(self):
        """
        Integer representation of the class instance
        :return:
        """
        # Raise error due to not implemented conversion
        raise NotImplementedError('Object cannot be converted to int')

    # def __bytes__(self):
    # def __float__(self):
    # etc....

    # Vessel methods
    def pump_in_fuel(self, quantity: float):
        self.fuel += quantity

    def pump_out_fuel(self):
        self.fuel = 0.0

    def discharge_passengers(self):
        self.passengers = []


if __name__ == '__main__':
    # Runtime tests will be here
    vsl = Vessel('Casandra')

