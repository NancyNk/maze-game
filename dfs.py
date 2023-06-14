from mazekit.mazeutil import MazeUtil
from PFMethods.utils import get_path

def dfs(maze, start=None, goal=None): #O(V+E) plus recursion overhead, we can say O(n^2) as V = n^2
    start = start or maze.props.start
    goal = goal or maze.props.goal
    predecessors = {start: None}   # dictionary that maps each node to its source node
    vis = set()  # set of visited nodes

    def isReachable(node=start) -> bool:
        #base cases
        if node in vis or not MazeUtil.is_valid_pos(maze, node):
            return False
        if node == goal:
            return True # if so, we will return that path later.
        
        # recursive case
        vis.add(node)
        for direction in MazeUtil.directions:
            adj = node[0] + direction[0], node[1] + direction[1]
            if isReachable(adj):
                predecessors[adj] = node
                return True
        return False
    
    return  get_path(predecessors, start, goal) if isReachable(start) else None 

