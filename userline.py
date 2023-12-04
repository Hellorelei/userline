'''userline, by Lorelei Chevroulet
This program aims to (1) automate the tasks of (2) querying whether a user's
account has any ongoing issues while providing a (3) basic text UI. To do so,
it (4) takes in a username and (5) iterates through all scripts stored in a
'modules' directory, present in the same directory as the program.

Scripts take in a 'username' and return an array of strings made of [0] a
value to be display and [1] its formatting (will most likely be colors).
'''
import time
from math import ceil
from pathlib import Path

INPUT_MODE = 'cli' # Sets username input mode to either 'cli' or 'card'
VERSION = '0.1'
MODULE_PATH = Path(__file__).parent / 'modules'
y = 0
hy = 0

class ansi:
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
    BLINK = '\033[5m'
    UNDERLINE = '\033[4m'
    RIGHT = '\033[C'
    #FRAMED = '\033[52m'
    CLEAR = '\033[J'
    CLINE = '\033[2K'
    UP = '\033[F'
    DOWN = '\033[E'
    ALLUP = '\033[H'
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
    modules = init()
    while 1:
        input('  Press any key to enter new username\n')
        print((ansi.UP + ansi.CLEAR) * (len(modules)+3))
        check(modules)

def init():
    printLogo()
    progressBar(0, 0, 12, 1, 1)
    time.sleep(.3)
    print(ansi.BOLD + '\nInitializing userline ' + VERSION + ansi.ENDC)
    time.sleep(.3)
    progressBar(2, 0, 12, 3, 0)
    modules = getModules()

    i = 0
    while i < 6:
        i += 0.4
        progressBar(6+i, 0, 12, 1, 0)
        time.sleep(.05)

    print(ansi.UP + ansi.CLINE)
    print('\n' * (len(modules)+1))
    return modules


def getModules():
    print('  Looking for modules...')
    module_list = []
    time.sleep(.2)
    print('    . modules found')
    x = 0
    for path in MODULE_PATH.iterdir():
        module_list.append(path)
        x += 1
        print(ansi.UP*x + ansi.CLINE + '    ' + str(x) + ' modules found' + ansi.DOWN*(x-1))
        print('      ❭ ' + str(path.name))
        progressBar(2, 2, 12, x+5, 0)
        time.sleep(.2)
    progressBar(4, 0, 12, x+5, 0)

    print(ansi.UP*(x+2) +  '  Importing modules...')
    print('    . modules imported')
    x = 0
    for module in module_list:
        x += 1
        print(ansi.UP*x + ansi.CLINE + '    ' + str(x) + ' modules imported' + ansi.DOWN*(x-1))
        print('      ❭ ' + ansi.B_GREEN + str(module.name) + ansi.ENDC)
        progressBar(4, 2, 12, x+5, 0)
        time.sleep(.2)
    progressBar(6, 0, 12, x+5, 0)
    print((ansi.UP + ansi.CLINE) * (x+5))
    return module_list

def getUsername():
    '''Obtains username and returns it using 'INPUT_MODE' method'''
    if INPUT_MODE == 'cli':     
        print((ansi.UP + ansi.CLINE)*2 + ansi.BOLD + '\n  Enter username: ' + ansi.UP + ansi.ENDC)
        return input(ansi.RIGHT*18)

def check(x):
    username = getUsername()
    print(ansi.UP + ansi.CLINE + ansi.BOLD + '  Username : ' + ansi.BR_GREEN + username + ansi.ENDC)
    print(ansi.UP)
    progressBar(1, 0, len(x)+1, 3, 1)
    j = 0
    for i in x:
        progressBar(j+1, 1, len(x)+1, 3+j, 0)
        time.sleep(.5)
        print('    ok!')
        progressBar(j+2, 0, len(x)+1, 4+j, 0)
        j += 1

def progressBar(step, h_step, steps, dis, r):
    global y
    global hy
    if r == 0:
        dy = y
        dhy = hy
    else:
        dy = 0
        dhy = 0

    x = 40 / steps
    y = ceil(x*step)
    hy = ceil(x*h_step)
    if y > 40:
        y = 40
    elif hy > 40:
        hy = 40
    elif hy + y > 40:
        hy = hy-1
    
    while (dy < y)|(dhy < hy):
        while (dhy < hy):
            dhy += 1
            progressBarDraw(y, dhy, dis)
            time.sleep(.1)
        while (dy < y):
            dy += 1
            if dhy > 0:
                dhy = dhy - 1
            progressBarDraw(dy, dhy, dis)
            time.sleep(.1)
        

    progressBarDraw(y, hy, dis)

def progressBarDraw(y, hy, dis):
    print(
        ansi.UP * dis + ansi.CLINE + ansi.ENDC 
        + '❬' + ('▬' * y) 
        + ('▰' * hy) + ansi.ENDC 
        + ansi.DIM + ('▬' * (40-(y+hy))) + ansi.ENDC 
        + '❭' + ansi.DOWN * (dis-1)
        )

def printLogo():
    print(
        ansi.BOLD + '─' * 78 + '\n' * 2 + r'''
                       ___        
     __ _____ ___ ____/ (_)__  ___ 
    / // (_-</ -_) __/ / / _ \/ -_)
    \_,_/___/\__/_/ /_/_/_//_/\__/ ''' + VERSION + '\n'*2
        + '\n' * 16 + ansi.UP * 16 + ansi.ENDC
        )
    time.sleep(.2)

# End-of-file (EOF)
if __name__ == "__main__":
    main()
