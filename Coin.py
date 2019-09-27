from CoinChange import coin_change

def main():
    coins = [5,6,7]  # coin denominations
    amount = 4  # amo0unt of money
    flag = False

    for i in range(len(coins)):
        if coins[i]>amount:
            flag = True

    if flag == True:
        print("Please enter amount greater than the available denominations..")
    else:
        print("No. of ways to form total: {}".format(coin_change(coins, amount)))


if __name__ == "__main__":
    main()


