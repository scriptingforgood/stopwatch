import os
import time

def cls():
    os.system('cls')

def clock():
    second = 1
    a = input('Press Enter to start, type \'no\' to cancel')
    while not a == 'no':
        try:
            print(second)
            time.sleep(0.99)
            second += 1
            if second == 300:
                a = input('repeat?')
                second = 1
        except KeyboardInterrupt:
            print('Stopped at '+str(second))
            b = input ('Restart? Type \'y\' to restart\n')
            if b == 'y':
                clock()
            else:
                break
clock()
