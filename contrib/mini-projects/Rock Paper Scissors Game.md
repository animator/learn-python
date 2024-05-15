```python
import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!", computer_choice
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!", computer_choice
    else:
        return "Computer wins!", computer_choice

def play_game():
    """Play the game and display the result."""
    user_choice = user_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result, computer_pick = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)
    computer_label.config(text=f"Computer picked: {computer_pick}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# User choice options
user_var = tk.StringVar()
user_var.set("rock")  # Default choice
choices = ["rock", "paper", "scissors"]
for choice in choices:
    rb = tk.Radiobutton(root, text=choice, variable=user_var, value=choice)
    rb.pack()

# Play button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

# Computer pick label
computer_label = tk.Label(root, text="", font=("Helvetica", 12))
computer_label.pack()

root.mainloop()
