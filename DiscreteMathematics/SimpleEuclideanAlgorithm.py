# -*- coding: utf-8 -*-

# Simple Euclidean Algorithm
#
# Computed the gcd of two given numbers


class EA:

    @staticmethod
    def gcd(int_a, int_b, check=True):
        """Calculates the Greatest Common Divisor of two given integers.
        set check to False to skip the sanity checks when calling the method
        within further recursion steps"""

        # Sanity Checks
        if check:
            for parameter in (int_a, int_b):
                if not isinstance(parameter, int):
                    print('Failed - parameter is no integer: %s' %parameter)
                    return False
                if not int_a >= 0:
                    print('Failed - parameter %d < 0' % parameter)
                    return False

            # Swap if the greater integer is the second parameter
            if not int_a > int_b:
                print('Swapping - %d < %d' % (int_a, int_b))
                int_a, int_b = int_b, int_a

        # Recursive GCD calculation
        rem = int_a % int_b

        if rem == 0:
            return int_b
        else:
            return EA.gcd(int_a=int_b, int_b=rem, check=False)
