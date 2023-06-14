import random
from typing import Optional
from mazekit.props import Props
class Maze:
    def __init__(self):
        self._grid =  []
        self._props = Props()

    @staticmethod
    def generate_maze(rows=None, cols=None) -> 'Maze': #O(n^2) # method used to generate the mazes randomly
        maze = Maze()
        if not rows or not cols:
            maze.props.rows = rows = random.randint(8, 50) # In case there is no rows is passed it will choose a randoom number between 8 and 50
            maze.props.cols = cols = random.randint(8, 50)# In case there is no columns is passed it will choose a randoom number between 8 and 50
        # print(f"Generating maze of size {rows}x{cols}\nto print it u can call print_grid()")
        maze.grid = [["." for _ in range(cols)] for _ in range(rows)] #O(n*m)
        maze.props.start = (0,0)
        while maze.props.goal == None or maze.props.goal == maze.props.start:
            maze.props.goal = (random.randint(0, rows-1), random.randint(0, cols-1)) # In case the goal was not specified it will choose a random number in the grid to make it the goal
        maze.props.invalid_count = int(rows * cols * 0.2) # used to specify the number of the walls(invalid positions) in the maze

        maze.props.invalid_positions = set()  # unique positions
        while len(maze.props.invalid_positions) < maze.props.invalid_count: #O(n)
            row = random.randint(0, rows-1)
            col = random.randint(0, cols-1)
            if (row, col) not in [maze.props.start, maze.props.goal]:
                maze.props.invalid_positions.add((row, col))

        for row, col in maze.props.invalid_positions: #O(n)
            maze.grid[row][col] = "X" # sets the invalid position with X

        maze.grid[maze.props.start[0]][maze.props.start[1]] = "S" # sets the start position with S
        maze.grid[maze.props.goal[0]][maze.props.goal[1]] = "E" # sets the Goal position with E
        return maze
        
    @staticmethod
    def read_maze(filename='../maze.txt') -> Optional['Maze']: #O(n^2) & may the input grid is invalid and return None
        try:
            maze = Maze()
            with open(filename,'r') as f:
                lines = f.readlines() #O(n) # used to read the lines of the opened maze
                maze.props.rows = len(lines) # used to set the variable rows with the number of rows in the read maze
                maze.props.cols = len(lines[0].strip("\n"))# used to set the variable columnns with the number of columns in the read maze
                maze.grid = [list(line.strip("\n")) for line in lines]

                if not maze.is_valid_grid(maze.grid): # To check if the maze is valid or not
                    print(f"Invalid maze")
                    raise SystemExit(1)
                
                for row in range(maze.props.rows):
                    for col in range(maze.props.cols):
                        if maze.grid[row][col] == 'S':
                            maze.props.start = (row, col)
                        elif maze.grid[row][col] == 'E':
                            maze.props.goal = (row, col)
                        elif maze.grid[row][col] == 'X':
                            maze.props.invalid_count += 1 # To determine the number of in valid positions in the given maze
                            maze.props.invalid_positions.add((row, col)) # ANd add the index of the invalid position
            return maze
        except OSError as e:
            print(f"Cannot open {filename}: {e.strerror}") # In Case the opened file cannot be read
            raise SystemExit(1)
        
    def is_valid_grid(self,grid) -> bool: #O(n^2)
        rows = len(grid)
        if not rows:
            return False
        len_of_row = len(grid[0])
        for row in grid:
            if len(row) != len_of_row:
                return False
        return True

    #some accessors/mutators
    @property # getter function
    def grid(self):
        return self._grid
    @grid.setter
    def grid(self, grid): 
        self._grid = grid
    @property
    def props(self):
        return self._props
    @staticmethod
    def print_grid(maze, filename=None): #O(n) used to print the maze
        for row in maze.grid:
            print("".join(row), file=filename, end="\n")
    
