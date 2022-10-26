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

def calc_e(phi:int)->int:
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e


"""
Should replace this function by bezout
Not efficient enough
"""
def calc_d(phi:int, e:int)->int:
    for d in range(phi, 1, -1):
        if e*d%phi == 1:
            return d

def __main__():
    pA = generate_prime()
    qA = generate_prime()
    print("Calc n")
    nA = pA * qA
    print("N done")
    print("calc phi")
    phi = (pA-1)*(qA-1)
    print("phi done")
    print("calc e")
    e = calc_e(phi)
    print("e done")
    print("calc d")
    d = calc_d(phi, e)
    print("d done")
    print(f"Your crypt key: e = {e}, n = {nA}")
    print(f"Your decrypt key: d = {d}")

"""
p = prime_input("p")
q = prime_input("q")
n = p*q
phi = (p-1)*(q-1)
e = calc_e(phi)
d = calc_d(phi, e)
"""

__main__()