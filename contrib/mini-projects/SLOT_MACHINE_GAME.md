"""
Slot Machine Game Guide

What is this Game?
This is a simple console-based slot machine game implemented in Python. It simulates a traditional slot machine where players can deposit money, place bets, and spin the slot machine to potentially win more money based on the symbols displayed.

Rules:
1. Deposit Money: Players start by depositing an amount of money to play with.
2. Place Bets: Players can bet on up to 3 lines with a minimum bet of $1 and a maximum bet of $150 per line.
3. Spin: Players spin the slot machine and the result is a 3x3 grid of symbols.
4. Winning: If the symbols in any of the lines bet on match, players win money based on the value of the symbols.

Way of Play:
1. Deposit: The player is prompted to deposit an initial amount of money.
2. Bet: The player chooses how many lines to bet on and how much to bet per line.
3. Spin: The player spins the slot machine, which generates a random 3x3 grid of symbols.
4. Outcome: The result is displayed, showing whether the player has won or lost. The player's balance is updated accordingly.
5. Repeat or Quit: The player can choose to spin again or quit. The game ends if the player runs out of money.

Detailed Steps:
1. Start the Game:
   - Run the main() function to start the game.
   - The player is asked to deposit an amount of money to begin.

2. Place Bets:
   - The player selects the number of lines to bet on (between 1 and 3).
   - The player specifies the amount to bet per line (between $1 and $150).

3. Spin the Slot Machine:
   - The slot machine generates a random 3x3 grid of symbols.
   - The outcome is displayed on the screen.

4. Check Winnings:
   - If any of the lines bet on have matching symbols, the player wins an amount calculated based on the symbol values and the bet amount.
   - The player's balance is updated with the winnings or losses.

5. Continue or Quit:
   - The player is asked if they want to spin again or quit.
   - If the player's balance reaches zero, the game ends automatically.

6. End of Game:
   - When the player chooses to quit or runs out of money, a final message thanking the player for playing is displayed.

This game is a fun way to simulate the experience of playing a slot machine, with simple rules and clear instructions for betting and spinning.
"""

import random

# Constants for the slot machine configuration
MAX_LINES = 3
MAX_BET = 150  # Maximum bet per line
MIN_BET = 1    # Minimum bet per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Symbols and their respective counts on the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Values assigned to each symbol for calculating winnings
symbol_value = {
    "A": 6,
    "B": 5,
    "C": 4,
    "D": 3
}

# Function to check if the player has won
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # Check each line the player has bet on
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

# Function to generate a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Populate the list of symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # Select random symbols for each column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

# Function to print the slot machine's result
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to get the deposit amount from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Function to get the number of lines to bet on from the user
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Function to get the bet amount per line from the user
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

# Function to handle the main betting and spinning process
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Sorry, you do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    else:
        print("You won on lines: 0")
    return winnings - total_bet

# Main function to start the slot machine game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        if balance <= 0:
            print("You have run out of money!")
            break
    print(f"You left with ${balance}")
    print("Thank you for playing!")

# Entry point of the program
main()
