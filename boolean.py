class MyClass:
    host = None
    port = None
    db_name = None

    def __bool__(self):
        """
        Representation in bool() method. Can be used to validate something
        :return:
        """
        return bool(self.host and self.port and self.db_name)


if __name__ == '__main__':
    # Launching our app
    mc = MyClass()
    mc.host = 'localhost'
    mc.port = 8080
    mc.db_name = 'my_db'

    print(bool(mc))

    if mc:
        print('Connector is ready')
