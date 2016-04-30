# -*- coding: utf-8 -*-

# The Diffie-Hellman Key Exchange
#
# The Diffie-Hellman Key Exchange solves the challenge to agree onto a secret
# key over a unsecure communication channel (known as Diffie-Hellman-problem).
# It's security is based on discrete logarithms over finite fields. It has been
# developed by Martin Hellman, Whitfield Diffie and Ralph Merkle at the
# University of Stanford.
#
# This method can be attacked by man-in-the-middle techniques. To avoid this,
# the use of additional security methods (such as signatures) is necessary.
# There exist several derived algorithms, such as ECDH (over elliptic curves)
# or Ephemeral Diffie-Hellman (used by TLS 1.2), which uses new domain
# parameters for each session.
#
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

        # ToDo: Generate a high prime number to use as p parameter
        self.prime = prime or pow(2, 19)-1
        self.alpha = alpha or randint(2, self.prime-2)
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
