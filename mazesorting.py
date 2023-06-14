from mazekit.maze import Maze
from mazekit.props import Props
from typing import List
import random

def is_harder(maze1:Maze, maze2:Maze) -> bool: # delegation to compare bwetween the mazes according to the diffuclity according to the number of invalid positions
    return Props.compare(maze1.props, maze2.props)

def quick_sort(array) : #O(nlogn)
        if len(array) <= 1:
            return array
        pivot = array[random.randint(0, len(array)-1)] # choose the pivot element randomly
        pivot, array[-1] = array[-1], pivot #shift to the end of the list
        left = [maze for maze in array[:-1] if not is_harder(maze, pivot)] # Create the left side which contains the number of invalid positions less than the randomly generated ppivot element
        right = [maze for maze in array[:-1] if is_harder(maze, pivot)]# Create the right side which contains the number of invalid positions grater than the randomly generated ppivot element
        return quick_sort(left) + [pivot] + quick_sort(right) #U sed to return the array of mazes sorted accordinng to the number of invalid positions

# sort the mazes based on the number of invalid positions (invalid_count)
def sort_maze(mazes:List['Maze']) -> List['Maze']: # Used to shuffle teh elements which is teh mazes as if they were sorted it will take much more time to sort them
    random.shuffle(mazes) #O(n)
    return quick_sort(mazes) #O(nlog(n))