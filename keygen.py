import math
import random
import time
from statistics import mean

"""
Naive approch
"""
def naive_is_prime(n: int)->bool:
    if n <= 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
    
"""
From wiki, 6k+-1 optimisation
"""
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def generate_prime()->int:
    print("Computing...")
    n = 0
    while not is_prime(n):
        n = random.getrandbits(40)
    print("done")
    return n