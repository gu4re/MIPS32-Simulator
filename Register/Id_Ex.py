from datetime import datetime
import time


class Id_Ex:
    def __init__(self):
        self.__cod_op = None
        self.__rd = None
        self.__rs = None
        self.__rt = None

    def read_cod_op(self):
        time.sleep(1)
        return self.__cod_op

    def read_rd(self):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ID_EX]: Read rd register '{self.__rd}'.")
        return self.__rd

    def read_rs(self):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ID_EX]: Read rs register '{self.__rs}'.")
        return self.__rs

    def read_rt(self):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ID_EX]: Read rt register '{self.__rt}'.")
        return self.__rt

    def write(self, new_cod_op, new_rd=None, new_rs=None, new_rt=None):
        time.sleep(1)
        self.__cod_op = new_cod_op
        self.__rd = new_rd
        self.__rs = new_rs
        self.__rt = new_rt
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ID_EX]: Save operation code '{new_cod_op}' and its details.")
