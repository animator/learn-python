# Rock Paper Scissors Game

This is a simple implementation of the classic rock-paper-scissors game in Python.

## Code Explanation:

In this section, we import the required libraries (`tkinter` for GUI and `random` for generating computer choices) and define two functions:

- `determine_winner(user_choice, computer_choice)`: 
    - This function determines the winner of the game based on the choices made by the user and the computer. 
    - It returns a tuple containing the result of the game and the computer's choice.

- `play_game()`: 
    - This function handles the gameplay logic. 
    - It gets the user's choice from the radio buttons, generates a random choice for the computer, determines the winner using the `determine_winner()` function, and updates the result and computer pick labels accordingly.

### Imports and Function Definitions:
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
```
### GUI Setup:
```python
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
```
- Here, we create the main window for the game using `tkinter.Tk()`. We set the title to "Rock Paper Scissors".
- We define a `StringVar` to store the user's choice and set the default choice to "rock".
- We create radio buttons for the user to choose from ("rock", "paper", "scissors") and pack them into the main window.
```
```
### Play Button and Result Labels:
```python
# Play button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

# Computer pick label
computer_label = tk.Label(root, text="", font=("Helvetica", 12))
computer_label.pack()
```
- We create a "Play" button that triggers the `play_game()` function when clicked, using `tkinter.Button`.
- We create two labels to display the result of the game (`result_label`) and the computer's choice (`computer_label`). Both labels initially display no text and are packed into the main window.
```
```

### Mainloop:
```python
root.mainloop()
```
- Finally, we start the Tkinter event loop using `root.mainloop()`, which keeps the GUI window open and responsive until the user closes it.
- 
