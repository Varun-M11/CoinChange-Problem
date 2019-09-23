from MinCoinsReq import find_min_coins, print_used_coins

def main2():
    amount = 13
    coins = [2, 3, 5]
    numOfCoins = len(coins)

    minNumCoins = [None for i in range(amount+1)]
    usedCoins = [None for i in range(amount+1)]

    print("Minimum no. of coins required: {}".format(find_min_coins(
        coins, amount, numOfCoins, minNumCoins, usedCoins)))

    print("THe required coins are: ", end="")
    print_used_coins(usedCoins, amount)


if __name__ == "__main__":
    main2()