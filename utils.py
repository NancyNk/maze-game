def get_path(predecessors,start,goal): #O(n) USed to print the path that the method used to reach the goal
    current = goal
    path = []
    while current != None:
        path.append(current)
        current = predecessors[current] #every element has a predecessor with the previous position
    return path[::-1] #reverse the path 