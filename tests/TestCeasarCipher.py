# -*- coding: utf-8 -*-

from unittest import TestCase

from HistoricCryptography.CaesarCipher import CeaserCipher


class TestCeasarCipher(TestCase):

    alphabet_ext = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                    'Y', 'Z', ' ', '.', ',', '!', '?')

    plain_text = 'CRYPTOISGREAT'
    cipher_text_2 = 'ETARVQKUITGCV'
    cipher_text_13 = 'PELCGBVFTERNG'

    plain_text_ext = '$ CRYPTO IS GREAT!'

    def testEncryption(self):
        cc = CeaserCipher()

        cc_ct_2 = cc.encrypt(plaintext=self.plain_text, key=2)
        self.assertEqual(self.cipher_text_2, cc_ct_2)

        cc_ct_13 = cc.encrypt(plaintext=self.plain_text, key=13)
        self.assertEqual(self.cipher_text_13, cc_ct_13)

    def testDecryption(self):
        cc = CeaserCipher()

        cc_pt_2 = cc.decrypt(ciphertext=self.cipher_text_2, key=2)
        self.assertEqual(self.plain_text, cc_pt_2)

        cc_pt_13 = cc.decrypt(ciphertext=self.cipher_text_13, key=13)
        self.assertEqual(self.plain_text, cc_pt_13)

    def testEncryptionDecryptionExtended(self):
        cc = CeaserCipher(alphabet=self.alphabet_ext)

        cc_ct_27 = cc.encrypt(plaintext=self.plain_text_ext, key=27)
        cc_pt_27 = cc.decrypt(ciphertext=cc_ct_27, key=27)

        self.assertNotEqual(cc_ct_27, self.plain_text_ext)
        self.assertEqual(self.plain_text_ext, cc_pt_27)
