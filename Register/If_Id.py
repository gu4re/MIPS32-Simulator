import time
from datetime import datetime


class If_Id:
    def __init__(self):
        self.__instruction = None

    def read_instruction(self):
        time.sleep(0.1)
        return self.__instruction

    def write_instruction(self, new_instruction):
        time.sleep(0.1)
        self.__instruction = new_instruction

    def clear(self):
        time.sleep(0.1)
        self.__instruction = None
        print(f"{datetime.now().strftime('[%H:%M:%S]')}[IF_ID]: Clear memory due to 'None' received.")
