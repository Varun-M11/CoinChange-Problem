from CoinChange import coin_change

flag = False

def main():
    coins = [5,2,1]  # coin denominations
    amount = 12  # amo0unt of money

    print("No. of ways to form total: {}".format(coin_change(coins, amount)))

    for i in range(len(coins)):
        if coins[i]>amount:
            flag = True


if flag == True:
    print("Please enter amount greater than the available denominations..")
else:
    if __name__ == "__main__":
        main()

