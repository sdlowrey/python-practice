from unittest import TestCase

from simplemath.prime import is_prime


class PrimeTests(TestCase):
    def test_base(self):
        for n in range(-1, 1):
            self.assertFalse(is_prime(n))

    def test_low_primes(self):
        for n in [2, 3, 5, 7]:
            self.assertTrue(is_prime(n))

    def test_non_prime(self):
        for n in [4, 6, 8, 9]:
            self.assertFalse(is_prime(n))
