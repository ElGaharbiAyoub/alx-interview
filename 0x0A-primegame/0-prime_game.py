#!/usr/bin/python3
"""
Prime Game
"""


def sieveOfEratosthenes(n):
    """
    Generate all primes up to n
    """
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p]):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    return primes


def isWinner(x, nums):
    """
    Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    primes = sieveOfEratosthenes(max(nums))
    for i in range(x):
        prime = sieveOfEratosthenes(nums[i])
        if sum(prime) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
