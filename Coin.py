from CoinChange import coin_change


def main():
    coins = [1, 2, 5]  # coin denominations
    amount = 12  # amount of money

    print("No. of ways to form total: {}".format(coin_change(coins, amount)))


if __name__ == "__main__":
    main()
