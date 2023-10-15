from datetime import datetime
import time


class Mem_Wb:
    def __init__(self):
        self.__destination = None
        self.__value = None

    def read_destination(self):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Read destination '{self.__destination}'.")
        return self.__destination

    def read_address_or_value(self):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Read value '{self.__value}'.")
        return self.__value

    def write(self, new_destination, new_value):
        time.sleep(1)
        self.__destination = new_destination
        self.__value = new_value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Save details related to '{new_destination}' register.")
