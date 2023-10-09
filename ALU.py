import datetime
import time


class ALU:

    @staticmethod
    def add(value_1, value_2):
        time.sleep(2)
        print(f"{datetime.datetime.now().strftime('[%H:%M:%S]')}"
              f"[ALU]: Result of operation is {value_1 + value_2}")
        return value_1 + value_2

    @staticmethod
    def multiply(value_1, value_2):
        time.sleep(2)
        print(f"{datetime.datetime.now().strftime('[%H:%M:%S]')}"
              f"[ALU]: Result of operation is {value_1 * value_2}")
        return value_1 * value_2

    @staticmethod
    def subtract(value_1, value_2):
        time.sleep(2)
        print(f"{datetime.datetime.now().strftime('[%H:%M:%S]')}"
              f"[ALU]: Result of operation is {value_1 - value_2}")
        return value_1 - value_2


class ConditionalALU:

    @staticmethod
    def compare(value_1, value_2):
        time.sleep(2)
        print(f"{datetime.datetime.now().strftime('[%H:%M:%S]')}"
              f"[ALU]: Result of condition is {value_1 - value_2 == 0}")
        return value_1 - value_2 == 0
