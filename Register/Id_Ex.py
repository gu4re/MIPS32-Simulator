class Id_Ex:
    def __init__(self):
        self.__cod_op = None
        self.__rd = None
        self.__rs = None
        self.__rt = None

    def read_cod_op(self):
        return self.__cod_op

    def read_rd(self):
        return self.__rd

    def read_rs(self):
        return self.__rs

    def read_rt(self):
        return self.__rt

    def write(self, new_cod_op, new_rd=None, new_rs=None, new_rt=None):
        self.__cod_op = new_cod_op
        self.__rd = new_rd
        self.__rs = new_rs
        self.__rt = new_rt
