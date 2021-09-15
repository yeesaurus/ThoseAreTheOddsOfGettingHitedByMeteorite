import random
import time


## vars
tries = 0
loopstatus = 1
x = 44
printer = False
randomvar = 0


## loop
start = time.time()
while (loopstatus <= x):
    randomvar = (random.randint(1, 2))
    if (loopstatus == x):
        end = time.time()
        printer = True
        print(printer)
        print(start - end)
        loopstatus = loopstatus + 1

    elif (randomvar == 1):
        loopstatus = loopstatus + 1
    elif (randomvar == 2):
        tries = tries + 1
        print(tries)
        loopstatus = 1
        



