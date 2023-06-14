from mazekit.maze import Maze
from typing import List, Tuple, Optional
class MazeGenerator:
    @staticmethod # to be accessed any where without making an object from it
    def generate_some_mazes(num_mazes=20) -> List['Maze']: # In case there is no number of mazes passed by the user to generate it will automatically generate 20 mazes
        #O(sz*n*m) or O(n^3), where sz -> num of mazes to generate, and (n,m) -> size of the grid generated.
        mazes = []
        for i in range(num_mazes):
            maze = Maze.generate_maze()
            mazes.append(maze) # used to insert the generated maze in the array of generated mazes
        return mazes 