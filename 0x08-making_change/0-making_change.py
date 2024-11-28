#!/usr/bin/python3
"""Calculate the number of coins needed to give change."""


def sort_coins(coins):
    for i in range(len(coins)):
        for j in range(len(coins)):
            if j + 1 >= len(coins):
                break
            elif coins[j] < coins[j + 1]:
                temp = coins[j]
                coins[j] = coins[j + 1]
                coins[j + 1] = temp
    return coins


def makeChange(coins, total):
    """Calculate the change to giv"""

    if total < 1:
        return 0
    # sort the coin list
    coins = sort_coins(coins)
    # print(coins)
    change = []
    ans = 0
    for i in range(len(coins)):
        while (ans + coins[i]) <= total:
            if (ans + coins[i]) == total:
                change.append(coins[i])
                return len(change)
            else:
                ans += coins[i]
                change.append(coins[i])
        # print(change)
    return -1
