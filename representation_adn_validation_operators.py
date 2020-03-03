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

    def __lt__(self, other):
        """
        Less than other
        :param other:
        :return:
        """
        return len(self.passengers) < len(other)

    # __le__ - less or equal, __eq__ - equal, __ne__ - not equal, __gt__ - greater than, __ge__ - greater or equal

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
    vsl.pump_in_fuel(10.5)
    vsl.passengers = [
        {
            'name': 'Peter'
        },
        {
            'name': 'Jessika'
        }
    ]

    print(vsl < [1, ])

