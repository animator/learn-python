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
