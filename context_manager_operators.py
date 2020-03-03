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

    def __enter__(self):
        """
        Context manager with START execution. We can add some launching processes and return some object, ex. cursor
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager with END execution. We can add some safe procedures for object/process completion,
        ex. db.close()
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        pass

    # Vessel methods
    def pump_in_fuel(self, quantity: float):
        self.fuel += quantity

    def pump_out_fuel(self):
        self.fuel = 0.0

    def discharge_passengers(self):
        self.passengers = []


if __name__ == '__main__':
    # Runtime tests will be here
    with Vessel(name='Calypso') as vsl:
        print(vsl.name)

