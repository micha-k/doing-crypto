# -*- coding: utf-8 -*-

# Trivium Stream Cipher
# https://de.wikipedia.org/wiki/Trivium_(Algorithmus)


class Trivium:

    # Registers: 93, 84 and 111 bits
    a = [0]*93
    b = [0]*84
    c = [0]*111

    def __init__(self, iv, key):
        self.iv = iv
        self.key = key

        # 80-bit IV into the first 80 locations of register A
        i = 0
        for bit in self.iv:
            self.a[i] = bit
            i += 1

        # 80-bit key into the first 80 locations of register B
        i = 0
        for bit in self.key:
            self.b[i] = bit
            i += 1

        # Three rightmost bits of register C to one
        self.c[108] = 1
        self.c[109] = 1
        self.c[110] = 1

        # Warm up: clock 4x 288 = 1152 times
        for i in xrange(1152):
            self.clock_registers()

    def clock_registers(self):

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
        result = []

        for bit in text:
            key = self.clock_registers()
            result.append((bit + key) % 2)

        return result
