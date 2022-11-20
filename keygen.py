import math
import random

def verify_key(d:int, e:int, phi:int)->bool:
    return (d*e)%phi == 1 and math.gcd(e, phi) == 1
    
"""
From wikipedia, 6k+-1 optimisation
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
    n = 0
    while not is_prime(n):
        n = random.getrandbits(10)
    return n

def calc_e(phi:int)->int:
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e
    return -1

def bezout(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    ob = b  # On enregistre le modulo d'origine
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # Si x negatif, on lui ajoute le modulo d'origine
    return lx

def generate_keys():
    '''
    Function who generate a set of public and private key
    '''
    p = generate_prime()
    q = generate_prime()
    if p == q:
        return generate_keys()
    n = p * q
    phi = (p-1) * (q-1)
    e = calc_e(phi)
    if e == -1:
        return generate_keys()
    d = bezout(e, phi)
    if not verify_key(d, e, phi):
        return generate_keys
    return ((e, n),(d, n))