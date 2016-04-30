# -*- coding: utf-8 -*-

from unittest import TestCase

from AsynchronousCryptography.DiffieHellmannKeyExchange \
    import DiffieHellmannKeyExchange


class TestDiffieHellmannKeyExchange(TestCase):

    def testDHKEwithSmallNumbers(self):
        # public DHKE parameters
        p = 29
        alpha = 2

        # secret key parameter chosen by Alice
        a = 5

        # secret key parameter chosen by Bob
        b = 12

        dhke = DiffieHellmannKeyExchange(prime=p, alpha=alpha, a=a, b=b)
        key1, key2 = dhke.do_key_exchange()

        self.assertEqual(key1, 16)
        self.assertEqual(key1, key2)

    def testDHKEwithoutKnownSecretParams(self):
        # public DHKE parameters
        p = 29
        alpha = 2

        dhke = DiffieHellmannKeyExchange(prime=p, alpha=alpha)
        key1, key2 = dhke.do_key_exchange()

        self.assertEqual(key1, key2)