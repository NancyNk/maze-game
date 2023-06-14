import random
from mazekit.maze import Maze
from mazekit.mazegenerator import MazeGenerator
from mazekit.mazesorting import sort_maze
from enum import Enum

class Option(Enum):
    easy = "easy"
    hard = "hard"

def get_maze(option:Option) -> 'Maze': #O(n^3)
    mazes = MazeGenerator.generate_some_mazes(20) #O(n^3)
    sorted_mazes = sort_maze(mazes) #O(n+nlog(n)) cauz of shuffling or O(nlog(n))
    index = 0
    sz = len(sorted_mazes)
    if option == "easy":
        index = random.randint(0, sz//2) # Used to choose any maze randomly form the left side of the sorted mazes
    elif option == "hard":
        index = random.randint(sz//2+1, sz-2) # Used to choose any maze randomly form the right side of the sorted mazes
    return sorted_mazes[index]