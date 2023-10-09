import time

from datetime import datetime


class PC:

    __counter = hex(0x0000)

    @staticmethod
    def update(actual_counter):
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[PC]: Updated.")
        PC.__counter = hex(int(actual_counter, 16) + 4)

    @staticmethod
    def read():
        return PC.__counter
