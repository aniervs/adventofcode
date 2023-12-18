from pydantic import BaseModel
from collections import deque
from heapq import heappush, heappop, heapify
input_file = open("day17.in", "r")

matrix = list(map(list, input_file.read().strip().split('\n')))
matrix = [[int(x) for x in row] for row in matrix]

n, m = len(matrix), len(matrix[0])

class AugmentedNode(BaseModel):
    row: int
    col: int
    dir: str
    cnt: int # number of steps taken so far in the current direction (limit = 3)
    
    def __hash__(self):
        return hash((self.row, self.col, self.dir, self.cnt))

    def __eq__(self, other):
        return (self.row, self.col, self.dir, self.cnt) == (other.row, other.col, other.dir, other.cnt)

    def __lt__(self, other):
        return (self.row, self.col, self.dir, self.cnt) < (other.row, other.col, other.dir, other.cnt)
    

    
priority_queue = []
distance = dict()
parent = dict()

heappush(priority_queue, (0, AugmentedNode(row=0, col=0, dir="RIGHT", cnt=0)))
distance[AugmentedNode(row=0, col=0, dir="RIGHT", cnt=0)] = 0

while len(priority_queue) > 0:
    dist, node = heappop(priority_queue)
    if dist > distance[node]:
        continue
    r, c, d, cnt = node.row, node.col, node.dir, node.cnt
    if r == n - 1 and c == m - 1 and cnt >= 4:
        print(node, dist)
        break 
    
    if d == "RIGHT":
        next_cell = (r, c+1)
        left_cell = (r-1, c)
        right_cell = (r+1, c)
        left_dir, right_dir = "UP", "DOWN"
    elif d == "LEFT":
        next_cell = (r, c-1)
        left_cell = (r+1, c)
        right_cell = (r-1, c)
        left_dir, right_dir = "DOWN", "UP"
    elif d == "UP":
        next_cell = (r-1,c)
        left_cell = (r, c-1)
        right_cell = (r, c+1)
        left_dir, right_dir = "LEFT", "RIGHT"
    elif d == "DOWN":
        next_cell = (r+1,c)
        left_cell = (r, c+1)
        right_cell = (r, c-1)
        left_dir, right_dir = "RIGHT", "LEFT"
    else:
        raise ValueError("Invalid direction")
        
    for new_cell, new_dir, new_cnt in zip([next_cell, left_cell, right_cell], [d, left_dir, right_dir], [cnt+1, 1, 1]):
        if new_dir != d and cnt < 4:
            continue 
        if 0 <= new_cell[0] < n and 0 <= new_cell[1] < m and new_cnt <= 10:
            new_node = AugmentedNode(row=new_cell[0], col=new_cell[1], dir=new_dir, cnt=new_cnt)
            new_dist = dist + matrix[new_cell[0]][new_cell[1]]
            if new_node not in distance or new_dist < distance[new_node]:
                parent[new_node] = node
                distance[new_node] = new_dist
                heappush(priority_queue, (new_dist, new_node))


input_file.close()
