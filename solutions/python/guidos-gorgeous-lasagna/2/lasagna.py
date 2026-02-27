"""Guido's Gorgeous Lasagna"""

# define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# define the 'PREPARATION_TIME' constant
PREPARATION_TIME = 2


# define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# define the 'preparation_time_in_minutes()' function
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Return the preparation time in minutes.

    :param number_of_layers: int number of layers for the lasagna.
    :return: int the preparation time derived from 'PREPARATION_TIME'.
    """
    return number_of_layers * PREPARATION_TIME


# define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Return the total number of minutes you've been cooking.

    :param number_of_layers: int the number of layers added to the lasagna.
    :param elapsed_bake_time: int the number of minutes the lasagna has been baking in the oven.
    :return: int the total number of minutes you've been cooking or the sum of your preparation time and the time the lasagna has already spent baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
