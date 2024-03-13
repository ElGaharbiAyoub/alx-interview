#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Prime Game
    """
    def isPrime(n):
        """
        Check if a number is prime
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(n):
        """
        Count the number of primes
        """
        count = 0
        for i in range(1, n + 1):
            if isPrime(i):
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primes = countPrimes(num)
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
