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
