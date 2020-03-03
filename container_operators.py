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

    def __len__(self):
        """
        len() instance representation
        :return:
        """
        return len(self.passengers)

    def __getitem__(self, item):
        """
        Find/get item using index or other "item" key/argument.
        :param item:
        :return:
        """
        # Let's create a universal key finder
        if isinstance(item, int):
            # This is a positional index. Find with the list search
            return self.passengers[item]

        elif isinstance(item, str):
            # This is a dict name value. Use dict search
            passenger = next(x for x in self.passengers if x['name'] == item)
            return passenger
        else:
            # Unknown index
            raise TypeError('Index should be a string or an integer')

    def __setitem__(self, key, value):
        """
        For setting new or existing dict item or list/tuple item
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError

    def __delitem__(self, key):
        """
        Remove one of the items
        :param key:
        :return:
        """
        if isinstance(key, int):
            del self.passengers[key]

        elif isinstance(key, str):
            for idx, val in enumerate(self.passengers):
                if val['name'] == key:
                    del self.passengers[idx]

        else:
            raise TypeError('Index should be a string or an integer')

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

    print(len(vsl))
    print(vsl['Jessika'])
    print(vsl[0])
    del vsl['Jessika']
    print(vsl.passengers)
