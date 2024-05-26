# Python Code For The Tic Tac Toe Game
# Tic Tac Toe Game

## Overview

### Objective
- Get three of your symbols (X or O) in a row (horizontally, vertically, or diagonally) on a 3x3 grid.

### Gameplay
- Two players take turns.
- Player 1 uses X, Player 2 uses O.
- Players mark an empty square in each turn.

### Winning
- The first player to align three of their symbols wins.
- If all squares are filled without any player aligning three symbols, the game is a draw.

```python
print("this game should be played by two people player1 takes x player2 takes o")
board = [['1','2','3'],['4','5','6'],['7','8','9']]
x = 'X'
o = 'O'
def displayBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("----------------------------------------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("----------------------------------------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("----------------------------------------")
def updateBoard(character,position):
    row = (position-1)//3
    column = (position-1)%3
    board[row][column] = character
def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return 1
        elif board[0][i] == board[1][i] == board[2][i]:
            return 1
    if board[0][2] == board[1][1] == board[2][0]:
        return 1
    elif board[0][0] == board[1][1] == board[2][2]:
        return 1
    return 0
def check_position(position):
    row = (position-1)//3
    column = (position-1)%3
    if board[row][column] == x or board[row][column] == o:
        return 0
    return 1
print("==============================welcome to tic tac toe game =====================")
counter = 0
while 1:
    if counter % 2 == 0:
        displayBoard()
        while 1:
            choice = int(input(f"player{(counter%2)+1},enter your position('{x}');"))
            if choice < 1 or choice > 9:
                print("invalid input oplease try againn")
            if check_position(choice):
                updateBoard(x,choice)
                if check_win():
                    print(f"Congratulations !!!!!!!!!!!Player {(counter % 2)+1} won !!!!!!!!!!")
                    exit(0)
                else :
                    counter += 1
                    break
            else:
                print(f"position{choice} is already occupied.Choose another position")
        if counter == 9:
            print("the match ended with draw better luck next time")
            exit(0)
    else:
        displayBoard()
        while 1:
            choice = int(input(f"player{(counter%2)+1},enter your position('{o}'):"))
            if choice < 1 or choice > 9:
                print("invalid input please try again")
            if check_position(choice):
                updateBoard(o,choice)
                if check_win():
                    print(f"congratulations !!!!!!!!!!!!!!! player{(counter%2)+1} won !!!!!!!!!!!!!1")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"position {choice} is already occupied.choose another position")
    print()
```
    
