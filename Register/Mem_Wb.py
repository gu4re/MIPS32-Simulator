class Mem_Wb:
    def __init__(self):
        self.__destination = 0
        self.__value = 0

    def read_destination(self):
        return self.__destination

    def read_value(self):
        return self.__value

    def write_destination(self, new_destination):
        self.__destination = new_destination

    def write_value(self, new_value):
        self.__value = new_value
