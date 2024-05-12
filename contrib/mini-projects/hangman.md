# Hangman Game

This is a simple Hangman game implemented in Python. 

### How to Play

- Guess letters to uncover the hidden word.
- You have a limited number of attempts to guess the word correctly.
- Have fun playing Hangman!

### Features

- Randomly generated words for each game.
- Visual representation of the Hangman.
- User-friendly interface.

### Code

The codebase is break down in two file `Hangman.py` and `main.py`.

`Hangman.py` contains implementation of hangman game.
and `main.py` contains basic code.


##### Here's the implementation of `Hangman.py`

```import random

class Hangman:
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry',
                 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine',
                 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine',
                 'watermelon', 'blueberry', 'blackberry', 'cranberry', 'boysenberry',
                 'pineapple', 'coconut', 'pear', 'plum', 'apricot', 'guava']

    MAX_INCORRECT_GUESSES = 6

    def __init__(self):
        self.word = random.choice(self.word_list)
        self.word_length = len(self.word)
        self.word_display = ['_' for _ in self.word]
        self.incorrect_guesses = 0
        self.guessed_letters = []

    def welcome(self):
        print('Welcome to Hangman!')
        print(f'The word has {self.word_length} letters.')
        print('Try to guess the word one letter at a time.')

    def display_word(self):
        print(' '.join(self.word_display))

    def update_word_display(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.word_display[i] = letter

    def play_game(self):
        self.welcome()

        while True:
            print(f'\nIncorrect guesses left: {self.MAX_INCORRECT_GUESSES - self.incorrect_guesses}')
            self.display_word()

            if '_' not in self.word_display:
                print('Congratulations! You guessed the word correctly!')
                break

            if self.incorrect_guesses >= self.MAX_INCORRECT_GUESSES:
                print(f'Sorry, you ran out of guesses. The word was {self.word}. Better luck next time!')
                break

            guess = input('Guess a letter: ').lower()

            if len(guess) != 1 or not guess.isalpha():
                print('Please enter a single letter.')
                continue

            if guess in self.guessed_letters:
                print('You already guessed that letter.')
                continue

            self.guessed_letters.append(guess)

            if guess in self.word:
                self.update_word_display(guess)
            else:
                print('Incorrect guess.')
                self.incorrect_guesses += 1
 ```


##### Here's the implementation of `main.py`

```
from hangman import Hangman

game = Hangman()
game.play_game()
```
