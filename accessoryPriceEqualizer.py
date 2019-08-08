# Tool to give "fair" prices based off 
import sys

PRIchance = .7
DUOchance = .5
TRIchance = .405
TETchance = .3

def equalizeFromBase(price):
    priceList = [price,0,0,0,0]
    priceList[1] = 2*price/PRIchance
    priceList[2] = (price+priceList[1])/DUOchance
    priceList[3] = (price+priceList[2])/TRIchance
    priceList[4] = (price+priceList[3])/TETchance
    return priceList

def main():
    priceList = equalizeFromBase(float(sys.argv[1]))
    print("Base: {}".format(priceList[0]))
    print("PRI:  {}".format(priceList[1]))
    print("DUO:  {}".format(priceList[2]))
    print("TRI:  {}".format(priceList[3]))
    print("TET:  {}".format(priceList[4]))


if __name__ == "__main__":
    main()
