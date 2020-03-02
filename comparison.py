class MyClass:
    some_val = None

    def __lt__(self, other):
        """
        Less than other
        :param other:
        :return:
        """
        return self.some_val < other

    def __le__(self, other):
        """
        Less or equal to other
        :param other:
        :return:
        """
        return self.some_val <= other

    def __eq__(self, other):
        """
        Equal to other
        :param other:
        :return:
        """
        print('Checking equal or not')

        # Let's cheat :)
        return self.some_val != other

    def __ne__(self, other):
        """
        Not equal to other
        :param other:
        :return:
        """
        return self.some_val != other

    def __gt__(self, other):
        """
        Greater than other
        :param other:
        :return:
        """
        return self.some_val > other

    def __ge__(self, other):
        """
        Greater or equal to other
        :param other:
        :return:
        """
        return self.some_val >= other


if __name__ == '__main__':
    # Launching our app
    mc = MyClass()

    mc.some_val = 10

    print(mc == 10)

    # All of them can be used for a complex objects comparison without values representation

