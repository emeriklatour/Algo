import random
import math


# Euclid's algorithm for determining the greatest common divisor
# Use iteration to make it faster for larger integers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(x, y):
    return x * y // gcd(x, y)


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


class RSA(object):
    def __init__(self, p, q, e=None):
        self._p = p
        self._q = q
        self._phi = (p - 1) * (q - 1)
        # choose exponent e such as gcd(phi, e) = 1
        self._e = self.find_e(e)
        self._n = p * q
        # private_key is d
        self.private_key = self.get_private_key()
        self.public_key = (self._n, self._e)

    def encrypt(self, plaintext):
        ciphertext = []
        for symbol in plaintext:
            encoded_char = chr(self.encrypt_symbol(ord(symbol)))
            ciphertext.append(encoded_char)
            # print(f'Symbol {symbol} is encoded as {ord(encoded_char)}={encoded_char}')
        return "".join(ciphertext)

    def encrypt_symbol(self, symbol):
        return RSA.power(symbol, self._e, self._n)

    def decrypt(self, ciphertext):
        plaintext = []
        for symbol in ciphertext:
            decoded_char = chr(self.decrypt_symbol(ord(symbol)))
            plaintext.append(decoded_char)
        return "".join(plaintext)

    def decrypt_symbol(self, symbol):
        return RSA.power(symbol, self.private_key, self._n)

    def get_private_key(self):
        c, d, dd = self.extended_euclid(self._e, self._phi)
        return d % self._phi

    @classmethod
    # algorithm computes, in addition to the
    # greatest common divisor (gcd)
    # of integers a and b, also the coefficients
    # of Bezout's identity, which are integers
    # x and y such that ax + by = gcd(a, b)
    def extended_euclid(cls, a, b):
        x = 1
        xx = 0
        y = 0
        yy = 1
        while b != 0:
            q = a // b
            a, b = b, a % b
            xx, x = x - q * xx, xx
            yy, y = y - q * yy, yy
        return a, x, y

    @classmethod
    def euclid(cls, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    # return x^k modulo n
    # rapid exponentiation by squaring
    def power(cls, x, k, n):
        result = 1
        while k > 0:
            if k % 2 != 0:  # if n is odd
                result = result * x % n
            x = x * x % n
            k = k // 2
        return result

    # Choose an integer e such that e and phi(n) are coprime
    def find_e(self, x):
        e = random.randrange(1, self._phi)
        # Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = math.gcd(e, self._phi)
        while g != 1:
            e = random.randrange(1, self._phi)
            g = math.gcd(e, self._phi)
        return x or e

    @classmethod
    # return x^k modulo n
    # rapid exponentiation by squaring - version 2
    def exponentiation(cls, x, k, n):
        if k == 0:
            return 1
        if k == 1:
            return x % n
        result = RSA.exponentiation(x, int(k / 2), n)
        result = (result * result) % n
        # if exponent is even value
        if k % 2 == 0:
            return result
        # if exponent is odd value
        else:
            return ((x % n) * result) % n


def run():
    FIRST_PRIMES = [2, 3, 5, 7, 13, 17, 19, 23]
    rsa = RSA(p=43, q=59, e=13)

    message = "stop"
    print(f"Original message is: {message}")
    encoded = rsa.encrypt(message)
    print(f"Encoded message is: {encoded}")
    decoded = rsa.decrypt(encoded)
    print(f"Decoded message is: {decoded}")
    print(f"Public key is: {rsa.public_key}")
    print(f"Private key is: {rsa.private_key}")


run()
