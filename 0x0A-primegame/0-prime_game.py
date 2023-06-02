#!/usr/bin/python3
"""Prime game module"""


def generate_primes(n):
    """ Generate a list of prime numbers up to n
    using the Sieve of Eratosthenes algorithm"""
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)

    return primes


def isWinner(x, nums):
    """Determines the winner of the prime game"""
    winner_counts = {'Maria': 0, 'Ben': 0}

    primes = generate_primes(max(nums))

    for i in range(x):
        n = nums[i]
        if n == 1 or n in primes:
            # If n is 1 or a prime number, Ben wins
            winner_counts['Ben'] += 1
        else:
            # If n is not a prime number, Maria wins
            winner_counts['Maria'] += 1

    if winner_counts['Maria'] > winner_counts['Ben']:
        return 'Maria'
    elif winner_counts['Maria'] < winner_counts['Ben']:
        return 'Ben'
    else:
        return None
