class Ex_Mem:
    def __init__(self):
        self.__cod_op = None
        self.__destination = None
        self.__address_or_value = None

    def read_cod_op(self):
        return self.__cod_op

    def read_destination(self):
        return self.__destination

    def read_address_or_value(self):
        return self.__address_or_value

    def write(self, cod_op, destination, address_or_value):
        self.__cod_op = cod_op
        self.__destination = destination
        self.__address_or_value = address_or_value
