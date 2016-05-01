# -*- coding: utf-8 -*-

# Trivium Stream Cipher
# https://de.wikipedia.org/wiki/Trivium_(Algorithmus)


class Trivium:

    def __init__(self, iv, key):
        """Initializes a new trivium setup with key and initialization vector.
        Both are supplied as 80bit arrays with either 0 or 1 on each bit."""

        # 80-bit IV into the first 80 locations of register A (93 bits)
        self.a = iv + [0]*13

        # 80-bit key into the first 80 locations of register B (84b its)
        self.b = key + [0]*4

        # Three rightmost bits of register C (111 bits) to one
        self.c = [0]*108 + [1]*3

    def warm_up(self):
        """Prepare the registers to en-/decrypt sensitive data by doing 4 full
        dryruns over the whole setup"""

        # Warm up: clock 4x 288 = 1152 times
        for i in xrange(1152):
            self.clock_registers()

    def clock_registers(self):
        """One run of the all three shift registers according to the Trivium
        specifications"""

        # shift register A
        and_input = (self.c[108] * self.c[109]) % 2
        output_c = (and_input + self.c[65] + self.c[110]) % 2
        new_bit = (output_c + self.a[68]) % 2

        self.a.pop()
        self.a.insert(0, new_bit)

        # shift register B
        and_input = (self.a[90] * self.a[91]) % 2
        output_a = (and_input + self.a[65] + self.a[92]) % 2
        new_bit = (output_a + self.b[77]) % 2

        self.b.pop()
        self.b.insert(0, new_bit)

        # shift register C
        and_input = (self.b[81] * self.b[82]) % 2
        output_b = (and_input + self.b[68] + self.b[83]) % 2
        new_bit = (output_b + self.c[86]) % 2

        self.c.pop()
        self.c.insert(0, new_bit)

        # key stream
        return (output_a + output_b + output_c) % 2

    def encrypt_decrypt(self, text):
        """Takes a plain text/cipher text as array of bits (1 or 0) and XORs
        it with the Trivium key stream. The result is returned as array of
        bits as well"""
        
        result = []

        for bit in text:
            key = self.clock_registers()
            result.append((bit + key) % 2)

        return result
