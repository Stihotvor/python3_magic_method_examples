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

    def __getattr__(self, item):
        """
        Called when unknown attribute is about to be fetched
        :param item:
        :return:
        """
        # Always raise this error in common situations
        raise AttributeError

    def __getattribute__(self, item):
        """
        Called when any attribute is about to be fetched
        :param item:
        :return:
        """
        # You can get attributes in a different way here
        # When an unknown attribute called, this method calls the above method
        print(f'Getting {item}')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """
        Setting the attribute with key - value
        :param key:
        :param value:
        :return:
        """
        print(f'Setting {key} with {value}')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        """
        Removes attribute from the class instance
        :param item:
        :return:
        """
        # This method will be called on "del attribute_name"
        super().__delattr__(item)

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
