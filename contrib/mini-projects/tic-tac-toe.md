import random


def play_duet():
    board = [' ' for x in range(9)]

    print("Enter the name of player 1")
    p1 = input()
    print("Enter the name of player 2")
    p2 = input()

    def print_board():
        row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
        row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
        row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def player_move(icon):
        if icon == 'X':
            number = p1
        elif icon == 'O':
            number = p2
        print('Your turn {}'.format(number))

        choice = int(input('Enter your move (1-9): ').strip())
        try:
            if board[choice - 1] == ' ':
                board[choice - 1] = icon

            else:
                print('That space is taken!')
        except(ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")





    def is_victory(icon):
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
                (board[3] == icon and board[4] == icon and board[5] == icon) or \
                (board[6] == icon and board[7] == icon and board[8] == icon) or \
                (board[0] == icon and board[3] == icon and board[6] == icon) or \
                (board[1] == icon and board[4] == icon and board[7] == icon) or \
                (board[2] == icon and board[5] == icon and board[8] == icon) or \
                (board[0] == icon and board[4] == icon and board[8] == icon) or \
                (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
        else:
            return False

    def is_draw():
        if ' ' not in board:
            return True
        else:
            return False

    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory('X'):
            print(p1, ' Wins! Congratulations!')
            break
        elif is_draw():
            print('The game is a draw!')
            break
        player_move('O')
        if is_victory('O'):
            print_board()
            print(p2, ' Wins! Congratulations!')
            break
        elif is_draw():
            print("It's a draw!")
            break


def play_comp():

    # Initialize the board
    board = [' ' for _ in range(9)]
    print("Enter the name of the player")
    s = input()

    def print_board(board):
        for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def check_winner(board, player):
        # Check rows, columns and diagonals
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

    def check_draw(board):
        return ' ' not in board

    def player_move(board):

        while True:
            print('Your turn', s)
            move = input("Enter your move (1-9): ")
            try:
                move = int(move) - 1
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("This spot is already taken!")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")

    def computer_move(board):
        available_moves = [i for i, spot in enumerate(board) if spot == ' ']
        move = random.choice(available_moves)
        board[move] = 'O'

    def tic_tac_toe():
        print_board(board)

        while True:
            # Player move
            player_move(board)
            print_board(board)
            if check_winner(board, 'X'):
                print(s, 'Wins! Congratulations!')
                break
            if check_draw(board):
                print("It's a draw!")
                break

            # Computer move
            computer_move(board)
            print("Computer's move:")
            print_board(board)
            if check_winner(board, 'O'):
                print("Computer wins! Better luck next time.")
                break
            if check_draw(board):
                print("It's a draw!")
                break

    if __name__ == "__main__":
        tic_tac_toe()



print("Welcome to Tic-Tac-Toe!")
print("Enter the number of players: ")
p = int(input())
if p == 1:
    play_comp()
elif p == 2:
    play_duet()
else:
    print("Only 2 players can play this game!!! Sorry")
