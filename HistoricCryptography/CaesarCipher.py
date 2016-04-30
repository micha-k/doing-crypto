# -*- coding: utf-8 -*-

# Caesar Cipher
#
# With a key value of 13 known as ROT13 as well.
#
# https://en.wikipedia.org/wiki/Caesar_cipher
# https://en.wikipedia.org/wiki/ROT13


class CaeserCipher:

    alphabet = ()

    def __init__(self, alphabet=False):
        if alphabet:
            self.alphabet = alphabet
        else:
            self.alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z')

        print self.alphabet

    def encrypt(self, plaintext, key):
        cipher_text = []

        for char in plaintext:
            try:
                cur_pos = self.alphabet.index(char)
            except ValueError:
                cipher_text.append(char)
            else:
                new_pos = (cur_pos+key) % len(self.alphabet)
                cipher_text.append(self.alphabet[new_pos])

        return ''.join(cipher_text)

    def decrypt(self, ciphertext, key):
        plain_text = []

        for char in ciphertext:
            try:
                cur_pos = self.alphabet.index(char)
            except ValueError:
                plain_text.append(char)
            else:
                new_pos = (cur_pos-key) % len(self.alphabet)
                plain_text.append(self.alphabet[new_pos])

        return ''.join(plain_text)
