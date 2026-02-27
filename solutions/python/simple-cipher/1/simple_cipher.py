"""Simple Cipher"""

import string
import secrets

KEY_CHARACTERS = string.ascii_lowercase
r = secrets.SystemRandom()


class Cipher:
    def __init__(self, key: str = None):
        if key is None:
            self.key = "".join(r.choices(KEY_CHARACTERS, k=100))
        else:
            self.key = key

    def encode(self, text: str) -> str:
        encoded = ""
        for i, character in enumerate(text):
            shift_distance = KEY_CHARACTERS.index(self.key[i%len(self.key)])
            encoded += KEY_CHARACTERS[(KEY_CHARACTERS.index(character) + shift_distance) % 26]
        return encoded

    def decode(self, text: str) -> str:
        decoded = ""
        for i, character in enumerate(text):
            shift_distance = KEY_CHARACTERS.index(self.key[i%len(self.key)])
            decoded += KEY_CHARACTERS[(KEY_CHARACTERS.index(character) - shift_distance)]
        return decoded
