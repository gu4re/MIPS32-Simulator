class Mem_Wb:
    def __init__(self, destination, value):
        self.__destination = destination
        self.__value = value

    def read_destination(self):
        return self.__destination

    def read_value(self):
        return self.__value
