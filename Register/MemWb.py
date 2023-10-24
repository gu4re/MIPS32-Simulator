from datetime import datetime
import time


class MemWb:
    def __init__(self):
        self.__destination = None
        self.__address_or_value = None

    def read_destination(self):
        time.sleep(0.1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Read destination '{self.__destination}'.")
        return self.__destination

    def read_address_or_value(self):
        time.sleep(0.1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Read value '{self.__address_or_value}'.")
        return self.__address_or_value

    def write(self, new_destination, new_address_or_value):
        time.sleep(0.1)
        self.__destination = new_destination
        self.__address_or_value = new_address_or_value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Save details related to '{new_destination}' register.")

    def clear(self):
        time.sleep(0.1)
        self.__destination = None
        self.__address_or_value = None
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[MEM_WB]: Clear memory due to 'None' received.")
