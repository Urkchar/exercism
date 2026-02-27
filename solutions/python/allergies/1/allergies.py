"""Allergies"""


class Allergies:

    def __init__(self, score):
        score %= 256

        self.eggs = False
        self.peanuts = False
        self.shellfish = False
        self.strawberries = False
        self.tomatoes = False
        self.chocolate = False
        self.pollen = False
        self.cats = False

        if score >= 128:
            self.cats = True
            score -= 128

        if score >= 64:
            self.pollen = True
            score -= 64

        if score >= 32:
            self.chocolate = True
            score -= 32

        if score >= 16:
            self.tomatoes = True
            score -= 16

        if score >= 8:
            self.strawberries = True
            score -= 8

        if score >= 4:
            self.shellfish = True
            score -= 4

        if score >= 2:
            self.peanuts = True
            score -= 2

        if score >= 1:
            self.eggs = True
            score -= 1

    def allergic_to(self, item):
        return getattr(self, item)

    @property
    def lst(self):
        return [item for item in list(self.__dict__.keys()) if getattr(self, item) is True]
