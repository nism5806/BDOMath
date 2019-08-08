# Tool to give "fair" accessory prices based off given price and enhancement level
# Assumes accessories are enhanced at softcap failstack and doesn't account for the cost of failstacks
# Usage: python accessoryPriceEqualizer [enhancement level (0-4)] [price]
import sys

PRIchance = .7
DUOchance = .5
TRIchance = .405
TETchance = .3

def equalize(startTier, startPrice):
    #initialize priceList
    priceList = [0,0,0,0,0]
    priceList[startTier] = startPrice
    #calculate base price
    if(startTier == 1):
        priceList[0] = PRIchance * startPrice / 2.0
    if(startTier == 2):
        # priceList[2] = (1+2/PRIchance)*price / DUOchance
        priceList[0] = DUOchance * startPrice / (1.0 + 2.0/PRIchance)
    if(startTier == 3):
        # priceList[3] = (1+(1+2/PRIchance)/DUOchance)*price / TRIchance
        priceList[0] = TRIchance * startPrice / (1.0 + (1.0 + 2.0/PRIchance)/DUOchance)
    if(startTier == 4):
        priceList[0] = TETchance * startPrice / (1.0 + (1.0 + (1.0 + 2.0/PRIchance)/DUOchance)/TRIchance)
    #calculate other prices
    chances = [PRIchance, DUOchance, TRIchance, TETchance]
    for i in range(1,len(priceList)):
        if(priceList[i]==0):
            priceList[i]=(priceList[0] + priceList[i-1])/chances[i-1]
    return priceList

def main():
    if(len(sys.argv)!=3 or int(sys.argv[1])<0 or int(sys.argv[1])>4):
        print("Usage: python accessoryPriceEqualizer.py [enhancement level (0-4)] [price]")
    else:
        priceList = equalize(int(sys.argv[1]), float(sys.argv[2]))
        print("Base: {}".format(priceList[0]))
        print("PRI:  {}".format(priceList[1]))
        print("DUO:  {}".format(priceList[2]))
        print("TRI:  {}".format(priceList[3]))
        print("TET:  {}".format(priceList[4]))


if __name__ == "__main__":
    main()
