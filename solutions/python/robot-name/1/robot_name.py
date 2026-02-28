"""Robot Name"""

import random
import string

names = []


class Robot:
    def __init__(self):
        naming = True
        while naming:
            name = random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + random.choice(string.digits) \
                 + random.choice(string.digits) \
                 + random.choice(string.digits)
            if name not in names:
                self.name = name
                names.append(name)
                naming = False

    def reset(self):
        naming = True
        while naming:
            name = random.choice(string.ascii_uppercase) \
                 + random.choice(string.ascii_uppercase) \
                 + random.choice(string.digits) \
                 + random.choice(string.digits) \
                 + random.choice(string.digits)
            if name not in names:
                self.name = name
                names.append(name)
                naming = False
