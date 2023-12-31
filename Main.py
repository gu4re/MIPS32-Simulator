import sys

from datetime import datetime
from library.colorama import Fore, Style
from Control.ControlUnit import ControlUnit

if __name__ == '__main__':
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Generating Circuit ... {Style.RESET_ALL}")
    ControlUnit.interpret(sys.argv)
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Starting program ... {Style.RESET_ALL}")
    ControlUnit.start()
