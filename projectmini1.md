```
import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "Congratulation, You win!"
    else:
        return " Better luck!! Computer wins!"

def play_game():
    print("hey guys, you are now playing Rock, Paper, Scissors using python!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))
        play_again = input(" want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("glad that you have played!!")

play_game()
```
