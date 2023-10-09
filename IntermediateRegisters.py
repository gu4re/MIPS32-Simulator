class If_Id:
    def __init__(self, instruction):
        self.__instruction = instruction

    def read(self):
        return self.__instruction


class Id_Ex:
    def __init__(self, cod_op, rd=None, rs=None, rt=None):
        self.__cod_op = cod_op
        self.__rd = rd
        self.__rs = rs
        self.__rt = rt

    def read_cod_op(self):
        return self.__cod_op

    def read_rd(self):
        return self.__rd

    def read_rs(self):
        return self.__rs

    def read_rt(self):
        return self.__rt


class Ex_Mem:
    def __init__(self, cod_op, destination, address_or_value):
        self.__cod_op = cod_op
        self.__destination = destination
        self.__address_or_value = address_or_value

    def read_cod_op(self):
        return self.__cod_op

    def read_destination(self):
        return self.__destination

    def read_address_or_value(self):
        return self.__address_or_value


class Mem_Wb:
    def __init__(self, destination, value):
        self.__destination = destination
        self.__value = value

    def read_destination(self):
        return self.__destination

    def read_value(self):
        return self.__value
