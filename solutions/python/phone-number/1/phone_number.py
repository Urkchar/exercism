"""Phone Number"""

class PhoneNumber:
    def __init__(self, number):

        # Cannot contain letters
        for character in number:
            if character.isalpha():
                raise ValueError("Phone numbers cannot have letters")

        # Cannot contain illegal characters
        legal_characters = "0123456789+()- ."
        for character in number:
            if character not in legal_characters:
                raise ValueError(f"Illegal character: '{character}'")

        # Remove the punctuation
        punctuation = ["+", "(", ")", "-", " ", "."]
        for punc in punctuation:
            number = number.replace(punc, "")

        # Invalid if 9 digits
        if len(number) == 9:
            raise ValueError(f"Invalid length: {len(number)}")

        # Invalid if greater than 11 digits
        if len(number) > 11:
            raise ValueError("Number too long")

        # Invalid if 11 digits and doesn't start with 1
        if len(number) == 11 and number[0] != "1":
            raise ValueError("11 digit numbers must start with 1")

        # Remove the international country code, if present
        if number.startswith("1") and len(number) == 11:
            number = number[1:]

        # Invalid if area code starts with 0 or 1
        if number[0] in "01":
            raise ValueError("Area code cannot start with 0 or 1")

        # Invalid if exchange code starts with 0 or 1

        if number[3] in "01":
            raise ValueError("Exchange code cannot start with 0 or 1")

        self.number = number
        self.area_code = number[0:3]

    def pretty(self):
        """(123)-456-7890"""
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
