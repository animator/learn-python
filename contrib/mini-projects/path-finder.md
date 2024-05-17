# Path Finder 
This Python script uses the curses library to visualize the process of finding a path through a maze in real-time within a terminal window. The program represents the maze as a list of lists, where each list represents a row in the maze, and each string element in the lists represents a cell in the maze. The maze includes walls (#), a start point (O), and an end point (X), with empty spaces ( ) that can be traversed.
##  The script includes the following main components:
- Visualization Functions: <br>
    print_maze(maze, stdscr, path=[]): This function is used to display the maze in the terminal. It utilizes color pairs to distinguish between the maze walls, the path, and unexplored spaces. The current path being explored is displayed with a different color to make it stand out.
  
- Utility Functions: <br>
    find_start(maze, start): This function searches the maze for the starting point (marked as O) and returns its position as a tuple (row, col). <br>
    find_neighbors(maze, row, col): This function identifies the valid adjacent cells (up, down, left, right) that can be moved to from the current position, 
    ignoring any walls or out-of-bound positions.
  
- Pathfinding Logic: <br>
    find_path(maze, stdscr): This function implements a Breadth-First Search (BFS) algorithm to find a path from the start point to the end point (X). It uses a 
    queue to explore each possible path sequentially. As it explores the maze, it updates the display in real-time, allowing the viewer to follow the progress 
    visually. Each visited position is marked and not revisited, ensuring the algorithm efficiently covers all possible paths without repetition.

Overall, the script demonstrates an effective use of the curses library to create a dynamic visual representation of the BFS algorithm solving a maze, providing both an educational tool for understanding pathfinding and an example of real-time data visualization in a terminal.

#### Below is the code of the path finder


```python
import curses
from curses import wrapper
import queue
import time

# Define the structure of the maze as a list of lists where each inner list represents a row.
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# Function to print the current state of the maze in the terminal.
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)  # Color pair for walls and free paths
    RED = curses.color_pair(2)   # Color pair for the current path

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)  # Print path character with red color
            else:
                stdscr.addstr(i, j*2, value, BLUE)  # Print walls and free paths with blue color

# Function to locate the starting point (marked 'O') in the maze.
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

# Function to find a path from start ('O') to end ('X') using BFS.
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)  # Get the start position

    q = queue.Queue()
    q.put((start_pos, [start_pos]))  # Initialize the queue with the start position

    visited = set()  # Set to keep track of visited positions

    while not q.empty():
        current_pos, path = q.get()  # Get the current position and path
        row, col = current_pos

        stdscr.clear()  # Clear the screen
        print_maze(maze, stdscr, path)  # Print the current state of the maze
        time.sleep(0.2)  # Delay for visibility
        stdscr.refresh()  # Refresh the screen

        if maze[row][col] == end:  # Check if the current position is the end
            return path  # Return the path if end is reached

        # Get neighbors (up, down, left, right) that are not walls
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor not in visited:
                r, c = neighbor
                if maze[r][c] != "#":
                    new_path = path + [neighbor]
                    q.put((neighbor, new_path))
                    visited.add(neighbor)

# Function to find the valid neighboring cells (not walls or out of bounds).
def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))
    return neighbors

# Main function to setup curses and run the pathfinding algorithm.
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Initialize color pair for blue
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Initialize color pair for red

    find_path(maze, stdscr)  # Find the path using BFS
    stdscr.getch()  # Wait for a key press before exiting

wrapper(main)  # Use the wrapper to initialize and finalize curses automatically.

```
         


