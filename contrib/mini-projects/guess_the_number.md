# Guess the Number Game

## Description
The "Guess the Number" game is a simple console-based game where the player has to guess a randomly generated number between 1 and 100. The player has 5 chances to guess the number. After each guess, the game provides feedback indicating whether the guess was too low, too high, or correct. If the player guesses the number correctly within 5 attempts, they win. If not, the game reveals the correct number and offers the player an option to play again.

## Prerequisites
- Python 3.x

## Installation
1. Save the game code in a file named `guess_the_number.py`.
## How to Run
1. Open a terminal or command prompt.
2. Navigate to the directory where you saved `guess_the_number.py`.
3. Run the file, where it is saved.

```

import random

def guess_the_number():
    while True:
        # Generate a random number between 1 and 100
        guess_number = random.randint(1, 100)
        
        # Give the player 5 chances to guess the number
        chances = 5

        print("Welcome to the Guess the Number game!")
        print("You have 5 chances to guess the number between 1 and 100.")

        for attempt in range(1, chances + 1):
            try:
                # Prompt the player to guess the number
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
                
                # Check if the guess is correct
                if guess == guess_number:
                    print(f"Congratulations! You got it right. The number was {guess_number}.")
                    break
                elif guess < guess_number:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            # If the player didn't guess the number in 5 attempts, they lose
            print(f"Oh no, you lost! The number was {guess_number}.")

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break
        # Run the game
guess_the_number()
```
Output when you run the file:
Welcome to the Guess the Number game!
You have 5 chances to guess the number between 1 and 100.
Attempt 1: Enter your guess: 50
Too low!
Attempt 2: Enter your guess: 75
Too high!
Attempt 3: Enter your guess: 60
Too low!
Attempt 4: Enter your guess: 65
Congratulations! You got it right. The number was 65.
Do you want to play again? (yes/no): no
Thank you for playing! Goodbye!
