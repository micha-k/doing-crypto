# -*- coding: utf-8 -*-

from unittest import TestCase

from SynchronousStreamCiphers.Trivium import Trivium


class TestTrivium(TestCase):

    plain_text = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    iv = (1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0)

    key = (0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
           0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
           0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
           0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0)

    def testEncryptionDecryption(self):
        t1 = Trivium(iv=self.iv, key=self.key)
        ct = t1.encrypt_decrypt(text=self.plain_text)
        self.assertNotEqual(self.plain_text, ct)

        t2 = Trivium(iv=self.iv, key=self.key)
        pt = t2.encrypt_decrypt(text=ct)
        self.assertEqual(self.plain_text, pt)
