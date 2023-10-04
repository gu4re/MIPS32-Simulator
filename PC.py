class PC:

    __counter = hex(0x0000)

    @staticmethod
    def update(actual_counter):
        PC.__counter = hex(int(actual_counter, 16) + 4)

    @staticmethod
    def read():
        return PC.__counter
