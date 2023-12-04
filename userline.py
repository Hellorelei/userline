'''userline, by Lorelei Chevroulet
This program aims to (1) automate the tasks of (2) querying whether a user's
account has any ongoing issues while providing a (3) basic text UI. To do so,
it (4) takes in a username and (5) iterates through all scripts stored in a
'modules' directory, present in the same directory as the program.

Scripts take in a 'username' and return an array of strings made of [0] a
value to be display and [1] its formatting (will most likely be colors).
'''
import time
from pathlib import Path

INPUT_MODE = 'cli' # Sets username input mode to either 'cli' or 'card'
VERSION = '0.1'
MODULE_PATH = Path(__file__).parent / 'modules'

class bcolors:
    HEADER = '\033[95m'
    BR_MAGENTA = '\033[95m'
    BR_BLUE = '\033[94m'
    BR_CYAN = '\033[96m'
    BR_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    #FRAMED = '\033[52m'
    CLEAR = '\033[2K'
    UP = '\033[2K'
    TEST = '\033[F'
    B_GREEN = '\033[42m'
    B_RED = '\033[41m'
    B_BLUE = '\033[44m'
    B_MAGENTA = '\033[45m'
    B_CYAN = '\033[46m'
    BBR_GREEN = '\033[102m'
    BBR_RED = '\033[101m'
    BBR_BLUE = '\033[104m'
    BBR_MAGENTA = '\033[105m'
    BBR_CYAN = '\033[106m'

def main():
    '''Main script'''
    printLogo()
    print(bcolors.BOLD + 'Initializing userline ' + VERSION + bcolors.ENDC)
    modules = getModules()
    username = getUsername()
    print(bcolors.BOLD + 'Username : ' + bcolors.BR_GREEN + username + bcolors.ENDC)
    print('')

def getModules():
    print(' Looking for modules...')
    progressBar()
    return 5

def getUsername():
    '''Obtains username and returns it using 'INPUT_MODE' method'''
    if INPUT_MODE == 'cli':     
        print(bcolors.BOLD + 'Enter username: ' + bcolors.ENDC)
        return input()

def progressBar():
    i = 0
    print(bcolors.DIM + '   >' + '»' * 40 + '<' + bcolors.ENDC)
    while i < 40:
        i += 1
        print(bcolors.TEST + bcolors.B_MAGENTA + '  (' + '»' * i + bcolors.ENDC)
        time.sleep(.1)

def printLogo():
    print(bcolors.BOLD + r'''
                   ___         
 __ _____ ___ ____/ (_)__  ___ 
/ // (_-</ -_) __/ / / _ \/ -_)
\_,_/___/\__/_/ /_/_/_//_/\__/ 
          ''')

# End-of-file (EOF)
if __name__ == "__main__":
    main()
