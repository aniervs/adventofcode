from collections import deque 

input_file = open("day16.in", "r")

matrix = list(map(list, input_file.read().strip().split('\n')))
n, m = len(matrix), len(matrix[0])

Q = deque()
vis = set() # set of visited states (row, col, direction)

def process(r, c, d):
    neighbor_states = []
    if d == "RIGHT":
        if c+1 == m:
            return
        new_char = matrix[r][c+1]
        if new_char in ["-", "."]:
            neighbor_states.append((r, c+1, d))
        elif new_char == "/":
            neighbor_states.append((r, c+1, "UP"))
        elif new_char == "\\":
            neighbor_states.append((r, c+1, "DOWN"))
        elif new_char == "|":
            neighbor_states.append((r, c+1, "UP"))
            neighbor_states.append((r, c+1, "DOWN"))
    elif d == "LEFT":
        if c-1 < 0:
            return
        new_char = matrix[r][c - 1]
        if new_char in ["-", "."]:
            neighbor_states.append((r, c-1, d))
        elif new_char == "/":
            neighbor_states.append((r, c-1, "DOWN"))
        elif new_char == "\\":
            neighbor_states.append((r, c-1, "UP"))
        elif new_char == "|":
            neighbor_states.append((r, c-1, "UP"))
            neighbor_states.append((r, c-1, "DOWN"))
    elif d == "UP":
        if r-1 < 0:
            return
        new_char = matrix[r-1][c]
        if new_char in ["|", "."]:
            neighbor_states.append((r-1, c, d))
        elif new_char == "/":
            neighbor_states.append((r-1, c, "RIGHT"))
        elif new_char == "\\":
            neighbor_states.append((r-1, c, "LEFT"))
        elif new_char == "-":
            neighbor_states.append((r-1, c, "LEFT"))
            neighbor_states.append((r-1, c, "RIGHT"))
    elif d == "DOWN":
        if r+1 == n:
            return
        new_char = matrix[r+1][c]
        if new_char in ["|", "."]:
            neighbor_states.append((r+1, c, d))
        elif new_char == "/":
            neighbor_states.append((r+1, c, "LEFT"))
        elif new_char == "\\":
            neighbor_states.append((r+1, c, "RIGHT"))
        elif new_char == "-":
            neighbor_states.append((r+1, c, "LEFT"))
            neighbor_states.append((r+1, c, "RIGHT"))
    else:
        raise Exception("Invalid direction")

    for neighbor_state in neighbor_states:
        if neighbor_state in vis:
            continue
        vis.add(neighbor_state)
        Q.append(neighbor_state)


def find_count():
    cnt = 0
    for r in range(n):
        for c in range(m):
            is_visited = False
            for d in ['RIGHT', 'LEFT', 'UP', 'DOWN']:
                if (r, c, d) in vis:
                    is_visited = True
                    break
            if is_visited:
                cnt += 1
    return cnt

def solve(row, col, dir):
    global Q, vis
    Q = deque()
    vis = set()
    process(row, col, dir)
    while len(Q) > 0:
        r, c, d = Q.popleft()
        process(r, c, d)
    return find_count()

ans = 0
for c in range(m):
    ans = max(
        ans, solve(row=-1, col=c, dir="DOWN")
    )
    ans = max(
        ans, solve(row=n, col=c, dir="UP")
    )
    ans = max(
        ans, solve(row=c, col=-1, dir="RIGHT")
    )
    ans = max(
        ans, solve(row=c, col=m, dir="LEFT")
    )
    
print(ans)
        
input_file.close()