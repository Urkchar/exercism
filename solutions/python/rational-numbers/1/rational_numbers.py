"""Rational Numbers"""

from __future__ import division
import math

class Rational:
    """
    A rational number is defined as the quotient of two integers a and b, called the numerator and
    denominator, respectively, where b != 0.
    """
    def __init__(self, numer, denom):
        self.numer, self.denom = self.reduce(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        """
        r1 = a1 / b1
        r2 = a2 / b2
        r1 + r2 = a1 / b1 + a2 / b2 = (a1 * b2 + a2 * b1) / (b1 * b2)
        """
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        """
        r1 = a1 / b1
        r2 = a2 / b2
        r1 - r2 = a1 / b1 - a2 / b2 = (a1 * b2 - a2 * b1) / (b1 * b2)
        """
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        """
        r1 = a1 / b1
        r2 = a2 / b2
        r1 * r2 = (a1 * a2) / (b1 * b2)
        """
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __truediv__(self, other):
        """
        r1 = a1 / b1
        r2 = a2 / b2
        r1 / r2 = (a1 * b2) / (a2 / b1) if a2 * b1 != 0
        """
        if other.numer * self.denom != 0:
            new_numer = self.numer * other.denom
            new_denom = other.numer * self.denom
            return Rational(new_numer, new_denom)

    def __abs__(self):
        """|r| = |a|/|b|"""
        new_numer = abs(self.numer)
        new_denom = abs(self.denom)
        return Rational(new_numer, new_denom)

    def __pow__(self, power: int):
        """Rational to an integer power"""

        # Negative integer power
        # r = a/b
        # n: int
        # r^n = (b^m) / (a^m) where m = |n|
        if isinstance(power, int) and power < 0:
            m = abs(power)
            new_numer = self.denom ** m
            new_denom = self.numer ** m

        # Non-negative integer power
        # r = a/b
        # n: int
        # r^n = (a^n) / (b^n)
        if isinstance(power, int):
            new_numer = self.numer ** power
            new_denom = self.denom ** power
            return Rational(new_numer, new_denom)

        raise TypeError("power must be an integer")

    def __rpow__(self, base):
        """Integer to a rational power
        r = a/b
        x: real number
        x^(a/b) = root(x^a, b) where root(p, q) is the qth root of p
        """
        return root(base ** self.numer, self.denom)

    def reduce(self, numer: int, denom: int) -> tuple:
        """Puts a rational number in lowest terms"""

        # Zero in the numerator reduces to 0/1
        if numer == 0:
            denom = 1

        # Same numerator and denominator reduces to 1/1
        if numer == denom:
            numer = 1
            denom = 1

        # Negative numerator and denominator changes to positive for both
        if numer < 0 and denom < 0:
            numer = abs(numer)
            denom = abs(denom)

        # The negative sign belongs with the numerator, not the denominator
        if numer > 0 and denom < 0:
            numer *= -1
            denom = abs(denom)

        # Reduce top-heavy Rational ie 14/7 -> 2/1
        while numer % denom == 0:
            old_numer = numer
            old_denom = denom
            numer //= denom
            denom //= denom
            if numer == old_numer and denom == old_denom:
                break

        # Reduce bottom-heavy Rational ie 3/9 -> 1/3
        while math.gcd(numer, denom) != 1:
            divisor = math.gcd(numer, denom)
            numer, denom = numer // divisor, denom // divisor

            # The negative sign belongs with the numerator, not the denominator
            if numer > 0 and denom < 0:
                numer *= -1
                denom = abs(denom)

        return numer, denom


def root(p, q):
    """Finds the qth root of p"""
    return p ** (1 / q)
