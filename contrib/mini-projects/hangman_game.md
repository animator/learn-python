# Hangman - Movies Edition
The Hangman game script is a simple Python program designed to let players guess movie titles. It starts by importing the random module to select a movie from a predefined list. The game displays the movie title as underscores and reveals correctly guessed letters. Players have six attempts to guess the entire title, entering one letter at a time. The script checks if the input is valid, updates the list of guessed letters, and adjusts the number of attempts based on the correctness of the guess. The game continues until the player either guesses the title correctly or runs out of attempts. Upon completion, it congratulates the player for a correct guess or reveals the movie title if the attempts are exhausted. The main execution block ensures the game runs only when the script is executed directly.Below is first the code and then an explanation of the code and its components.

## Code

```
import random

def choose_movie():
    movies = ['avatar', 'titanic', 'inception', 'jurassicpark', 'thegodfather', 'forrestgump', 'interstellar', 'pulpfiction', 'shawshank']
    return random.choice(movies)

def display_word(movie, guessed_letters):
    display = ""
    for letter in movie:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman_movies():
    movie = choose_movie()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman - Movies Edition!")
    print("Try to guess the name of the movie. You have 6 attempts.")

    while attempts > 0:
        print("\n" + display_word(movie, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in movie:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the movie name. You have {attempts} attempts left.")
        else:
            print(f"Good guess! '{guess}' is in the movie name.")

        if "_" not in display_word(movie, guessed_letters):
            print(f"\nCongratulations! You guessed the movie '{movie.capitalize()}' correctly!")
            break

    if attempts == 0:
        print(f"\nSorry, you ran out of attempts. The movie was '{movie.capitalize()}'.")

if __name__ == "__main__":
    hangman_movies()
```

## Code Explanation

### Importing the Random Module

```python

import random

```

The `random` module is imported to use the `choice` function, which will help in selecting a random movie from a predefined list.

### Choosing a Movie

```python

def choose_movie():

movies = ['avatar', 'titanic', 'inception', 'jurassicpark', 'thegodfather', 'forrestgump', 'interstellar', 'pulpfiction', 'shawshank']

return random.choice(movies)

```

The `choose_movie` function returns a random movie title from the `movies` list.

### Displaying the Word

```python

def display_word(movie, guessed_letters):

display = ""

for letter in movie:

if letter in guessed_letters:

display += letter + " "

else:

display += "_ "

return display

```

The `display_word` function takes the movie title and a list of guessed letters as arguments. It constructs a string where correctly guessed letters are shown in their positions, and unknown letters are represented by underscores (`_`).

### Hangman Game Logic

```python

def hangman_movies():

movie = choose_movie()

guessed_letters = []

attempts = 6

print("Welcome to Hangman - Movies Edition!")

print("Try to guess the name of the movie. You have 6 attempts.")

while attempts > 0:

print("\n" + display_word(movie, guessed_letters))

guess = input("Guess a letter: ").lower()

if len(guess) != 1 or not guess.isalpha():

print("Please enter a single letter.")

continue

if guess in guessed_letters:

print("You've already guessed that letter.")

continue

guessed_letters.append(guess)

if guess not in movie:

attempts -= 1

print(f"Sorry, '{guess}' is not in the movie name. You have {attempts} attempts left.")

else:

print(f"Good guess! '{guess}' is in the movie name.")

if "_" not in display_word(movie, guessed_letters):

print(f"\nCongratulations! You guessed the movie '{movie.capitalize()}' correctly!")

break

if attempts == 0:

print(f"\nSorry, you ran out of attempts. The movie was '{movie.capitalize()}'.")

```

The `hangman_movies` function manages the game's flow:

1. It selects a random movie title using `choose_movie`.

2. Initializes an empty list `guessed_letters` and sets the number of attempts to 6.

3. Prints a welcome message and the initial game state.

4. Enters a loop that continues until the player runs out of attempts or guesses the movie title.

5. Displays the current state of the movie title with guessed letters revealed.

6. Prompts the player to guess a letter.

7. Validates the player's input:

- Ensures it is a single alphabetic character.

- Checks if the letter has already been guessed.

8. Adds the guessed letter to `guessed_letters`.

9. Updates the number of attempts if the guessed letter is not in the movie title.

10. Congratulates the player if they guess the movie correctly.

11. Informs the player of the correct movie title if they run out of attempts.

### Main Execution Block

```python

if __name__ == "__main__":

hangman_movies()

```
## Conclusion
This block ensures that the game runs only when the script is executed directly, not when it is imported as a module.

## Output Screenshots:

![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/a7af1f7e-c80e-4f83-b1f7-c7c5c72158b4)
![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/082e54dc-ce68-48fd-85da-3252d7629df8)



## Conclusion

This script provides a simple yet entertaining Hangman game focused on guessing movie titles. It demonstrates the use of functions, loops, conditionals, and user input handling in Python.


