# -*- coding: utf-8 -*-

from unittest import TestCase

from SynchronousStreamCiphers.Trivium import Trivium


class TestTrivium(TestCase):

    plain_text = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    iv = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1]

    key = [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,
           0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,
           0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,
           0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]

    def testTriviumRegisters(self):
        t = Trivium(iv=self.iv, key=self.key)

        self.assertEqual(93, len(t.a))
        self.assertEqual(84, len(t.b))
        self.assertEqual(111, len(t.c))

        self.assertEqual(self.iv, t.a[:80])
        self.assertEqual(self.key, t.b[:80])
        self.assertEqual([1, 1, 1], t.c[-3:])

        t.warm_up()

        self.assertNotEqual(self.iv, t.a[:80])
        self.assertNotEqual(self.key, t.b[:80])
        self.assertNotEqual([1, 1, 1], t.c[-3:])

    def testEncryptionDecryption(self):
        t1 = Trivium(iv=self.iv, key=self.key)
        t1.warm_up()
        ct = t1.encrypt_decrypt(text=self.plain_text)
        self.assertNotEqual(self.plain_text, ct)

        t2 = Trivium(iv=self.iv, key=self.key)
        t2.warm_up()
        pt = t2.encrypt_decrypt(text=ct)
        self.assertEqual(self.plain_text, pt)
