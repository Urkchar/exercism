# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed_letters = []

    def guess(self, char):

        if self.remaining_guesses < 0:
            raise ValueError("You have already lost.")
        if self.status == STATUS_WIN:
            raise ValueError("You have already won.")
        
        # If they guess a correct letter
        if char in self.word:
            # Guessing a previously correct letter is a failed guess
            if char in self.guessed_letters:
                self.remaining_guesses -= 1
            else:
                self.guessed_letters.append(char)
        # If they don't guess a correct letter
        else:
            self.guessed_letters.append(char)
            self.remaining_guesses -= 1

        if self.word == self.get_masked_word():
            self.status = STATUS_WIN

        if self.remaining_guesses <= 0 and self.status != STATUS_WIN:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        masked_word = self.word[::]
        for char in self.word:
            if char not in self.guessed_letters:
                masked_word = masked_word.replace(char, "_")
        return masked_word

    def get_status(self):
        return self.status


# game = Hangman("foo")
# game.guess("f")
# game.guess("o")
# print(game.status)