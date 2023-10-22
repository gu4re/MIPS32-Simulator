import time
from datetime import datetime


class PC:

    def __init__(self):
        self.__counter = hex(0x0000)

    def update(self, actual_counter):
        time.sleep(0.2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[PC]: Updated.")
        self.__counter = hex(int(actual_counter, 16) + 4)

    def read(self):
        return self.__counter
