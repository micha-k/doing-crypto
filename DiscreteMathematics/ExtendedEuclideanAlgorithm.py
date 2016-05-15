# -*- coding: utf-8 -*-

# Extended Euclidean Algorithm
#
# Computed the gcd and the modular inverse of two given numbers. Used amongst
# other within the RSA crypto system.
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm


class EEA:

    def __init__(self, r0, r1):

        # Swap if the greater integer is the second parameter
        if not r0 > r1:
            print('Swapping - %d < %d' % (r0, r1))
            r0, r1 = r1, r0

        # Algorithm data structure
        self.i = 1
        self.data = dict()
        self.data['r'] = [r0, r1]
        self.data['q'] = [False, False]
        self.data['s'] = [1, 0]
        self.data['t'] = [0, 1]

    def run_eea(self):

        # step counter
        self.i += 1
        print('Round: %d:' % self.i)

        # workaround: extend arrays
        for char in ('r', 'q', 's', 't'):
            self.data[char].append(False)

        # step calculations
        self.data['r'][self.i] = self.data['r'][self.i-2] % \
                                 self.data['r'][self.i-1]

        self.data['q'][self.i-1] = (self.data['r'][self.i-2] -
                                    self.data['r'][self.i]) / \
                                    self.data['r'][self.i-1]

        self.data['s'][self.i] = self.data['s'][self.i-2] - (
                                 self.data['q'][self.i-1] *
                                 self.data['s'][self.i-1])

        self.data['t'][self.i] = self.data['t'][self.i-2] - (
                                 self.data['q'][self.i-1] *
                                 self.data['t'][self.i-1])

        print('%d = %d * %d + %d' % (self.data['r'][self.i-2],
                                     self.data['q'][self.i-1],
                                     self.data['r'][self.i-1],
                                     self.data['r'][self.i]))
        print('%d = %d * %d + %d * %d' % (self.data['r'][self.i],
                                          self.data['s'][self.i],
                                          self.data['r'][0],
                                          self.data['t'][self.i],
                                          self.data['r'][1]))

        # recursive eea
        if self.data['r'][self.i] == 0:
            return (self.data['r'][self.i-1],
                    self.data['s'][self.i-1],
                    self.data['t'][self.i-1])
        else:
            return self.run_eea()
