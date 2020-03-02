class MyClass:
    def __new__(cls, *args, **kwargs):
        """
        New instance initialization started here
        :param args:
        :param kwargs:
        """
        print('Class instance creation')
        return object.__new__(cls)

    def __init__(self):
        """
        Class instance initialized here
        """
        print('Class initialized')

    def __del__(self):
        """
        Class instance destruction method. Note: exceptions skipped by an interpreter.
        :return:
        """
        print('Some safe destruction procedures started')
        print('Some safe destruction procedures completed')
        print('Class instance destructed')


if __name__ == '__main__':
    # Launching our app
    mc = MyClass()
