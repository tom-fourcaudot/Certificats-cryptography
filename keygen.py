import math
import random

'''
Verify if the generated key is correct
@param d, e, phi: the key param
@return : true if the key is correct 
'''
def verify_key(d:int, e:int, phi:int)->bool:
    return (d*e)%phi == 1 and math.gcd(e, phi) == 1
    
'''
Test if a number is prime
@param n : the number
@return : True if n is prime
'''
def is_prime(n: int) -> bool:
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

'''
Generate a prime number with 2**10 bits
@return : a prime number
'''
def generate_prime()->int:
    n = 0
    while not is_prime(n):
        n = random.getrandbits(10)
    return n

'''
Compute e parameter in key with pgcd(e, phi) = 1
@param phi : the phi parameter
@return : E parameter if exist, else -1
'''
def calc_e(phi:int)->int:
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e
    return -1

'''
It's the extended euclyd algorithm to calculate D
@param a, b : bezout paraeter
@return : the parameter D
'''
def bezout(a: int, b: int)-> int:
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


'''
Generate a paire of key for RSA
@return : the correct pair of key -> ((e, n), (d, n))
'''
def generate_keys()->tuple:
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