# -*- coding: utf-8 -*-

from unittest import TestCase

from DiscreteMathematics.SimpleEuclideanAlgorithm import EA


class TestEA(TestCase):

    def testGCDCalculation(self):

        # Test gcd calculation
        self.assertEqual(3, EA.gcd(21, 9))
        self.assertEqual(6, EA.gcd(30, 84))
        self.assertEqual(7, EA.gcd(973, 301))

        # Test error handling
        self.assertFalse(EA.gcd('a', 9))
        self.assertFalse(EA.gcd(-21, 9))
