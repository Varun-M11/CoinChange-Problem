from MinCoinsReq import find_min_coins, print_used_coins

def main2():
    amount = 13
    coins = [2, 3, 5]
    numOfCoins = len(coins)

    minNumCoins = [None for i in range(amount+1)]
    usedCoins = [None for i in range(amount+1)]

    flag = False

    for i in range(len(coins)):
        if coins[i] > amount:
            flag = True
            
    if flag == True:
        print("Please enter amount greater than the available denominations..")
    else:
        print("Minimum no. of coins required: {}".format(find_min_coins(
            coins, amount, numOfCoins, minNumCoins, usedCoins)))
        
        print("The required coins are: ", end="")
        print_used_coins(usedCoins, amount)


if __name__ == "__main__":
    main2()
