"""Robot Name"""

import random
import string


class Robot:
    names_in_use = set()
    def __init__(self):
        self.give_name()

    def generate_name(self) -> str:
        """Return a string containing 2 random uppercase letters followed by 3 random digits."""
        return "".join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))

    def give_name(self):
        """Assign a unique name to the Robot."""
        while True:
            name = self.generate_name()
            if name not in self.names_in_use:
                self.name = name
                self.names_in_use.add(name)
                break

    def reset(self):
        """Change the name of the Robot to a new name."""
        # Store the old name so that it can be removed from the new list of names
        old_name = self.name

        # Give a new name
        self.give_name()

        # Remove the old name from the names in use
        self.names_in_use.remove(old_name)


# Asserting that each robot has a unique name
# robots = []
# for _ in range(100000):
#     robots.append(Robot())
# print(len(robots[0].names_in_use))   # 100000
