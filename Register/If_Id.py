class If_Id:
    def __init__(self):
        self.__instruction = None

    def read_instruction(self):
        return self.__instruction

    def write_instruction(self, new_instruction):
        self.__instruction = new_instruction
