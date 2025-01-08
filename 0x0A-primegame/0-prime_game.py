#!/usr/bin/python3
"""prime game."""


def isWinner(x, nums):
    """
    the game hase 2 players: [Maria, and  Bob]
    fide the winner of the game after 'x' rounds.
    Args:
      x: the number of rounds to be played
      nums: a list of limits for each round
    Return:
      the player who won the most rounds.
    """
    # create players
    player1 = {'name': "Maria", "wins": 0}
    player2 = {'name': "Ben", "wins": 0}
    # set first prime to 2

    for i in range(x):
        p = 2
        # load all numbers
        board = list(j for j in range(1, (nums[i] + 1)))
        while p * p <= nums[i]:
            # get all factors of current prime number
            not_primes = [c for c in range(p * p, nums[i] + 1, p)]

            # clear all  factors of current prime from board
            board = list(set(board) - set(not_primes))
            p += 1

        # get rounds winner
        if (len(board) - 1) % 2 == 0:
            player2['wins'] += 1
        else:
            player1['wins'] += 1

    if player1['wins'] >= player2['wins']:
        return player1['name']
    return player2['name']
