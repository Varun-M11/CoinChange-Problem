# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount

def coin_change(coins, amount):

    # init the combination array (list)
    combinations = [0 for i in range(amount + 1)]
    combinations[0] = 1  # base condition

    for coin in coins:     # coin = current coin  and  coins is the set of coins
        for i in range(1, len(combinations)):
            if coin <= i:
                combinations[i] += combinations[i - coin]

                # final result at combinations[amount] since 'amount' is the last index
    return combinations[amount]
