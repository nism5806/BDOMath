# returns chance of obtaining failstack for Black Desert Online
# usage: python failstacker.py [starting stack] [goal stack] [enhancement level to attempt (0-5 = +15-PEN)]
# only supports failing to +15-PEN on weapons or armor

import sys
from failstack import getStack

def stackChance(start, end, enhance):
    power = 1
    power += enhance
    current = start
    chance = 1.0
    while(current < end):
        failChance = 1.0 - getStack(current, enhance)
        chance *= failChance
        current += power
    return chance


def main():
    if(len(sys.argv)!=4 or int(sys.argv[3])<0 or int(sys.argv[3])>5):
        print('usage: python failstacker.py [starting stack] [goal stack] [enhancement level to attempt (0-5 = +15-PEN)]')
    else:
        print(stackChance(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))

if __name__ == "__main__":
    main()

