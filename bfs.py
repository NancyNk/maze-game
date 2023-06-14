from mazekit.mazeutil import MazeUtil
from collections import deque
from typing import List, Tuple
from PFMethods.utils import get_path


def bfs(maze, start=None, goal=None): #O(V+E), but V is n^2, and E is at most 4 edges, so it's O(n^2)
    start = start or maze.props.start
    goal = goal or maze.props.goal
    queue = deque()
    queue.append(start)
    predecessors = {start: None}
    vis = set()
    while queue:
        current_cell = queue.popleft()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        if current_cell not in vis:
            vis.add(current_cell)
            for direction in MazeUtil.directions:
                neighbour = current_cell[0] + \
                    direction[0], current_cell[1] + direction[1]
                if MazeUtil.is_valid_pos(maze, neighbour) and neighbour not in vis:
                    queue.append(neighbour)
                    predecessors[neighbour] = current_cell
    return None
