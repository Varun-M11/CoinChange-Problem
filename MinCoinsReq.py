# Function to find out minimum numbers of coins required to make
# the change for the amount.

def find_min_coins(coins, amount, numOfCoins, minNumCoins, usedCoins):
    minNumCoins[0] = 0

    for i in range(1, amount+1):
        minNumCoins[i] = 99999

    for i in range(1, amount+1):
        for j in range(0, numOfCoins):
            if coins[j] <= i:
                sub_res = minNumCoins[i-coins[j]]

                if sub_res != 99999 and sub_res+1 < minNumCoins[i]:
                    minNumCoins[i] = sub_res + 1
                    usedCoins[i] = coins[j]

    return minNumCoins[amount]

def print_used_coins(usedCoins, amount):
    while amount > 0:
        print(usedCoins[amount], end=" ")
        amount -= usedCoins[amount]
