from sys import argv as av
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def start(av):
    try:
        f = open(".not", "r")

        print(bcolors.BOLD + bcolors.HEADER + f.read(11) + bcolors.ENDC, end="")
        print(bcolors.OKBLUE + f.read(3) + bcolors.ENDC, end="")
        print(bcolors.WARNING + f.read() + bcolors.ENDC)
        f.close
    except:
        f = open(".not", "a")
        note = input()
        date = datetime.now().strftime("%d/%m %H:%M") + " >> "

        f.write(date)
        f.write(note)
        f.close()

if __name__ == "__main__":
    start(av)