from random import choice


class HangmanGame:
    # List of words the program randomly selects from
    word_list = ['python', 'java', 'kotlin', 'javascript']
    # Stores letters that the player guesses
    guessed_letters = []

    def __init__(self):
        self.magic_word = choice(self.word_list)
        self.covered = "-" * len(self.magic_word)
        self.tries = 8

    def check_words(self, inp):
        # Makes sure the input is valid before making checks
        good_input = self.verify_input(inp)
        if good_input:
            # Checks each letter in selected word
            for i in range(len(self.magic_word)):
                if self.magic_word[i] == inp:
                    # Checks if letter is already revealed
                    if self.has_letter(i):
                        break
                    # Reveals letter if it matches
                    else:
                        self.covered = self.covered[:self.magic_word.index(inp)] + inp \
                                       + self.covered[self.magic_word.index(inp) + 1:]
                else:
                    continue
            # Reduces number of tries by 1 if letter is not in word
            if inp not in self.magic_word:
                self.tries -= 1
                print("No such letter in the word")

    def verify_input(self, inp):
        # Handles invalid user inputs
        correct = False
        if len(inp) > 1:
            print("You should input a single letter")
        elif inp.isupper() or not inp.isalpha():
            print("It is not an ASCII lowercase letter")
        elif inp in self.guessed_letters:
            print("You already typed this letter")
        else:
            self.guessed_letters.append(inp)
            correct = True
        return correct

    def has_letter(self, pos):
        # Handles logic if user inputs an already guessed letter
        if self.magic_word[pos] == self.covered[pos]:
            self.tries -= 1
            print("No improvements")
            return True
        else:
            return False

    def game(self):
        # Main game loop
        while self.tries > 0:
            print()
            print(self.covered)
            # Read user input for as long as there is an input
            try:
                guess = input("Input a letter: ")
            except EOFError:
                break
            self.check_words(guess)
            # Break out of game loop if all characters are revealed
            if "-" not in self.covered:
                print("You survived!\n")
                break
        # Ends the game if user runs out of tries
        if self.tries == 0:
            print("You lost!\n")

    def start_game(self):
        # Menu loop
        print("H A N G M A N")
        while True:
            command = input('Type "play" to play the game, "exit" to quit: ')
            if command == "play":
                self.game()
            if command == "exit":
                break


# Initializes game
HangmanGame().start_game()
