# -*- coding: utf-8 -*-

from unittest import TestCase

from DiscreteMathematics.ExtendedEuclideanAlgorithm import EEA


class TestEEA(TestCase):

    def testGCDCalculation(self):

        eea1 = EEA(973, 301)
        (gcd1, s1, t1) = eea1.run_eea()
        self.assertEqual(7, gcd1)
        self.assertEqual(13, s1)
        self.assertEqual(-42, t1)

        eea2 = EEA(301, 973)
        (gcd2, s2, t2) = eea2.run_eea()
        self.assertEqual(gcd1, gcd2)
        self.assertEqual(s1, s2)
        self.assertEqual(t1, t2)
