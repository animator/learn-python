import random

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    @staticmethod
    def generate_empty_grid():
        return [[0 for _ in range(9)] for _ in range(9)]

    @staticmethod
    def is_valid_move(grid, row, col, num):
        # Check if the number is already present in the row, column, or 3x3 subgrid
        return (num not in grid[row] and
                num not in (grid[i][col] for i in range(9)) and
                num not in (grid[i][j] for i in range(row - row % 3, row - row % 3 + 3)
                            for j in range(col - col % 3, col - col % 3 + 3)))

    @staticmethod
    def generate_sudoku():
        grid = Sudoku.generate_empty_grid()
        Sudoku.solve_sudoku(grid)
        Sudoku.remove_cells(grid, random.randint(30, 45))  # Adjust the range for the number of empty cells
        return grid

    @staticmethod
    def solve_sudoku(grid):
        empty_cell = Sudoku.find_empty_cell(grid)
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in random.sample(range(1, 10), 9):
            if Sudoku.is_valid_move(grid, row, col, num):
                grid[row][col] = num
                if Sudoku.solve_sudoku(grid):
                    return True
                grid[row][col] = 0
        return False

    @staticmethod
    def find_empty_cell(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return None

    @staticmethod
    def remove_cells(grid, num_cells_to_remove):
        for _ in range(num_cells_to_remove):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if grid[row][col] != 0:
                grid[row][col] = 0

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(" ".join(map(str, row)))

def main():
    print("Generating Sudoku puzzle...")
    sudoku_grid = Sudoku.generate_sudoku()
    print("Sudoku puzzle:")
    Sudoku.print_grid(sudoku_grid)

    user_input = input("\nWould you like to see the solution? (yes/no): ").strip().lower()
    if user_input in ['yes', 'y']:
        solved_grid = [row[:] for row in sudoku_grid]  # Create a copy of the grid to solve
        if Sudoku.solve_sudoku(solved_grid):
            print("Sudoku solution:")
            Sudoku.print_grid(solved_grid)
        else:
            print("No solution found.")
    else:
        print("Solution not displayed.")

if __name__ == "__main__":
    main()
