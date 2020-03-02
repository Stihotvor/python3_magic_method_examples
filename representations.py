class MyClass:
    some_var = None

    def __repr__(self):
        """
        Defines beautiful representation of a class
        :return:
        """
        return f"<class 'MyClass'>"

    def __str__(self):
        """
        Represents string value of the object
        :return:
        """
        return str(100)

    def __bytes__(self):
        """
        Represents the object after bytes conversion
        :return:
        """
        return bytes(self.some_var)

    def __format__(self, format_spec):
        """
        Represents the object as a formated string
        :param format_spec:
        :return:
        """
        # See https://docs.python.org/3.7/library/string.html#formatspec :)
        pass


if __name__ == '__main__':
    # Launching our app
    mc = MyClass()
    mc.some_var = 10

    # Let's get representation of int
    print(repr(int))
    print(repr(mc))
    print(str(mc))
    print(bytes(mc))

