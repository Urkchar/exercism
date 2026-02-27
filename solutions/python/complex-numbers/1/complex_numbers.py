"""Complex Numbers"""

import math


class ComplexNumber:
    """A complex number is a number in the form a + b * i where a and b are real and i satisfies
    i^2 = -1."""
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        """
        The sum of two complex numbers involves adding their real and imaginary parts separately:
        (a + i * b) + (c + i * d) = (a + c) + (b + d) * i.
        """
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        new_real = a + c
        new_imaginary = b + d
        return ComplexNumber(new_real, new_imaginary)

    def __mul__(self, other):
        """
        Multiplication result is by definition
        (a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i.
        """
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        new_real = a * c - b * d
        new_imaginary = b * c + a * d
        return ComplexNumber(new_real, new_imaginary)

    def __sub__(self, other):
        """
        The difference of two complex numbers involves subtracting their real and imaginary parts
        separately:
        (a + i * b) - (c + i * d) = (a - c) + (b - d) * i.
        """
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        new_real = a - c
        new_imaginary = b - d
        return ComplexNumber(new_real, new_imaginary)

    def __truediv__(self, other):
        """
        Dividing a complex number a + i * b by another c + i * d gives:
        (a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i.
        """
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        new_real = (a * c + b * d) / (c ** 2 + d ** 2)
        new_imaginary = (b * c - a * d) / (c ** 2 + d ** 2)
        return ComplexNumber(new_real, new_imaginary)

    def __abs__(self):
        """
        The absolute value of a complex number z = a + b * i is a real number |z| = sqrt(a^2 + b^2).
        The square of the absolute value |z|^2 is the result of multiplication of z by its complex
        conjugate.
        """
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        """The conjugate of the number a + b * i is the number a - b * i"""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """
        Raising e to a complex exponent can be expressed as e^(a + i * b) = e^a * e^(i * b), the
        last term of which is given by Euler's formula e^(i * b) = cos(b) + i * sin(b).
        """
        a = self.real
        b = self.imaginary
        new_real = math.exp(a) * math.cos(b)
        new_imaginary = math.exp(a) * math.sin(b)
        return ComplexNumber(new_real, new_imaginary)
