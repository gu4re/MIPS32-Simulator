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

    def read_address_or_value(self, is_aux=False):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[{'EX_MEM/AUX' if is_aux else 'EX_MEM'}]: Read address or value '{self.__address_or_value}'.")
        return self.__address_or_value

    def write(self, new_cod_op, new_destination, new_address_or_value, is_aux=False):
        time.sleep(1)
        self.__cod_op = new_cod_op
        self.__destination = new_destination
        self.__address_or_value = new_address_or_value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[{'EX_MEM/AUX' if is_aux else 'EX_MEM'}]: Save result and details of operation code '{new_cod_op}'.")
