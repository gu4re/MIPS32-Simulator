import datetime
import time


class ConditionalALU:

    @staticmethod
    def compare(value_1, value_2):
        time.sleep(2)
        print(f"{datetime.datetime.now().strftime('[%H:%M:%S]')}"
              f"[ConditionalALU]: Result of condition is {value_2 - value_1 >= 0}")
        return value_2 - value_1 >= 0
