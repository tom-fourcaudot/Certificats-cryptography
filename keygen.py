import math
import random

class CA():
    def __init__(self):
        self.memo = {}

    def generate_keys(self, p:Person):
        p = generate_prime()
        q = generate_prime()
        n = p * q
        phi = (p-1) * (q-1)
        e = calc_e(phi)
        d = bezout(e, phi)
        self.memo[p.name]=((e, n),(d, n))

class Person():
    def __init__(self, name:str):
        self.name = name
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
    print("Computing...")
    n = 0
    while not is_prime(n):
        n = random.getrandbits(10)
    print("done")
    return n

def calc_e(phi:int)->int:
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e
            
#############################################################################
"""
Code from : https://gist.github.com/JekaDeka/c9b0f5da16625e3c7bd1033356354579
To refractor and understand
"""
def bezout(a: int, b: int)->int:
    """
    Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    return lx
#############################################################################

def crypt(mess:str, key: tuple)->list:
    e, n = key
    res = []
    for c in mess:
        c = int(c)
        res.append((c**e)%n)
    return res

def decrypt(mess:list, key: tuple)->str:
    d, n = key
    res = ""
    for c in mess:
        res+= str(((c**d)%n))
    return res

def __main__():
    mess = "2052"
    Alice = Person()
    Bob = Person()
    mess_c = crypt(mess, Alice.public)
    print(mess_c)
    print(decrypt(mess_c, Alice.private))
    


"""
p = prime_input("p")
q = prime_input("q")
n = p*q
phi = (p-1)*(q-1)
e = calc_e(phi)
d = calc_d(phi, e)
"""

__main__()