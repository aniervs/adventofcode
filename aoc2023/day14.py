from copy import deepcopy
input_file = open("day14.in", "r")

def compute_north_load(matrix):
    n, m = len(matrix), len(matrix[0])
    ans = 0
    for r in range(n):
        ans += matrix[r].count('O') * (n - r)
    return ans

def tilt(matrix, dir):
    n, m = len(matrix), len(matrix[0])
    if dir == "north":
        for c in range(m):
            for r in range(n):
                if matrix[r][c] == 'O':
                    r2 = r
                    while r2 > 0 and matrix[r2-1][c] == '.':
                        r2 -= 1
                    matrix[r][c] = '.'
                    matrix[r2][c] = 'O'
    elif dir == "south":
        for c in range(m):
            for r in range(n - 1, -1, -1):
                if matrix[r][c] == 'O':
                    r2 = r
                    while r2 < n - 1 and matrix[r2+1][c] == '.':
                        r2 += 1
                    matrix[r][c] = '.'
                    matrix[r2][c] = 'O'
    elif dir == "west":
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 'O':
                    c2 = c
                    while c2 > 0 and matrix[r][c2-1] == '.':
                        c2 -= 1
                    matrix[r][c] = '.'
                    matrix[r][c2] = 'O'
    elif dir == "east":
        for r in range(n):
            for c in range(m - 1, -1, -1):
                if matrix[r][c] == 'O':
                    c2 = c
                    while c2 < m - 1 and matrix[r][c2+1] == '.':
                        c2 += 1
                    matrix[r][c] = '.'
                    matrix[r][c2] = 'O'
    return matrix

def step(matrix):
    for dir in ['north', 'west', 'south', 'east']:
        matrix = tilt(deepcopy(matrix), dir)
    return matrix   
    
def encode(matrix):
    return "".join(["".join(row) for row in matrix])
def decode(matrix, n, m):
    return [list(matrix[m*i:m*(i + 1)]) for i in range(n)]
    
    
def process(matrix):
    seen_first = dict()
    record = []
    
    step_count = 0
    
    cycle_start = 0
    cycle_length = 0

    while True:
        encoded_matrix = encode(matrix)
        if encoded_matrix in seen_first:
            cycle_start = seen_first[encoded_matrix]
            cycle_length = step_count - cycle_start
            break 
        
        seen_first[encoded_matrix] = step_count
        record.append(matrix)
        matrix = step(matrix)
        step_count += 1
    
    return cycle_start, cycle_length, record, seen_first
    
def query(k, cycle_start, cycle_length, record):
    if k < cycle_start:
        print("Query:", k)
        return compute_north_load(record[k])
    else:
        print("Query:", (k - cycle_start) % cycle_length + cycle_start)
        return compute_north_load(record[(k - cycle_start) % cycle_length + cycle_start])

matrices = input_file.read().split("\n\n")

ans = 0
for matrix in matrices:
    matrix = list(map(list, matrix.split("\n")))[:-1]
    n, m = len(matrix), len(matrix[0])
    
    cycle_start, cycle_length, record, seen_first = process(deepcopy(matrix))

    print(f"Cycle start: {cycle_start}, Cycle length: {cycle_length}")
    ans += query(1000000000, cycle_start, cycle_length, record)

print(ans)
    
input_file.close()