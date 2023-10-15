from datetime import datetime
import time


class Ex_Mem:
    def __init__(self):
        self.__cod_op = None
        self.__destination = None
        self.__address_or_value = None

    def read_cod_op(self):
        time.sleep(1)
        return self.__cod_op

    def read_destination(self):
        time.sleep(1)
        return self.__destination

    def read_address_or_value(self):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[EX_MEM]: Read address or value '{self.__address_or_value}'.")
        return self.__address_or_value

    def write(self, new_cod_op, new_destination, new_address_or_value):
        time.sleep(1)
        self.__cod_op = new_cod_op
        self.__destination = new_destination
        self.__address_or_value = new_address_or_value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[EX_MEM]: Save result and details of operation code '{new_cod_op}'.")


class Aux_Ex_Mem(Ex_Mem):
    def __init__(self):
        super().__init__()

    def write(self, new_cod_op, new_destination, new_address_or_value):
        time.sleep(1)
        self.__cod_op = new_cod_op
        self.__destination = new_destination
        self.__address_or_value = new_address_or_value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[AUX_EX_MEM]: Save result and details of operation code '{new_cod_op}'.")

    # Need due to tunneling memory between EX and MEM phase
    def aux_to_ex_mem(self):
        cod_op_aux = self.__cod_op
        if cod_op_aux is not None:
            super().write(cod_op_aux, self.__destination, self.__address_or_value)
