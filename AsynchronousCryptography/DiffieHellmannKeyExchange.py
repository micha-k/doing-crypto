# -*- coding: utf-8 -*-

# ToDo: Write a few lines about the DHKE
# Wikipedia: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

from random import randint


class DiffieHellmannKeyExchange:

    prime = 0
    alpha = 0
    a = 0
    b = 0

    a_pub = 0
    b_pub = 0

    k_ab = 0
    k_ba = 0

    def __init__(self, prime=False, alpha=False, a=False, b=False):
        if prime:
            self.prime = prime
        else:
            # ToDo
            True

        if alpha:
            self.alpha = alpha
        else:
            # ToDo
            True

        self.a = a or randint(2, self.prime-2)
        self.b = b or randint(2, self.prime-2)

    def do_key_exchange(self):

        # Alice computes her public key
        # could by implemented more efficiently by using the z parameter
        # for pow() to calculate the modulus
        self.a_pub = pow(self.alpha, self.a) % self.prime
        print('Alice: a_pub = %d^%d = %d mod %d' % (self.alpha, self.a,
                                                    self.a_pub, self.prime))

        # Bob computes his public key
        self.b_pub = pow(self.alpha, self.b) % self.prime
        print('Bob: b_pub = %d^%d = %d mod %d' % (self.alpha, self.b,
                                                  self.b_pub, self.prime))

        # Alice computes the combined key with Bobs public key
        self.k_ab = pow(self.b_pub, self.a) % self.prime
        print('Alice: key_ab = %d^%d = %d mod %d' % (self.b_pub, self.a,
                                                     self.k_ab, self.prime))

        # Bob computes the combined key with Alice' public key
        self.k_ba = pow(self.a_pub, self.b) % self.prime
        print('Bob: key_ba = %d^%d = %d mod %d' % (self.a_pub, self.b,
                                                   self.k_ba, self.prime))

        return self.k_ab, self.k_ba
