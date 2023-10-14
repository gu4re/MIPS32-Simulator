class Mem_Wb:
    def __init__(self):
        self.__destination = None
        self.__value = None

    def read_destination(self):
        return self.__destination

    def read_value(self):
        return self.__value

    def write(self, new_destination, new_value):
        self.__destination = new_destination
        self.__value = new_value
