input_file = open("day10.in", "r")

matrix = []

row, col = None, None
for r, line in enumerate(input_file.readlines()):
    p = line.find('S')
    if p != -1:
        col = p
        row = r
    matrix.append(list(line.strip()))
input_file.close()
    
r, c = row, col
matrix[r][c] = 'F'
where = 'below'
length = 0

circuit = set()

while True:
    circuit.add((r, c))
    if matrix[r][c] == '|':
        if where == 'below':
            r -= 1 
        elif where == 'above':
            r += 1
    elif matrix[r][c] == '-':
        if where == 'lt':
            c += 1
        elif where == 'rt':
            c -= 1
    elif matrix[r][c] == 'L':
        if where == 'above':
            c += 1
            where = 'lt'
        elif where == "rt":
            r -= 1 
            where = 'below'
    elif matrix[r][c] == 'J':
        if where == "above":
            c -= 1 
            where = 'rt'
        elif where == 'lt':
            r -= 1
            where = 'below'
    elif matrix[r][c] == '7':
        if where == "below":
            c -= 1
            where = 'rt'
        elif where == "lt":
            r += 1
            where = 'above'
    elif matrix[r][c] == 'F':
        if where == "below":
            c += 1
            where = 'lt'
        elif where == "rt":
            r += 1
            where = 'above'

    if row == r and col == c:
        break          

n, m = len(matrix), len(matrix[0])

ans = 0
for r in range(n):
    cnt = 0
    for c in range(m):
        if (r, c) in circuit:
            if matrix[r][c] != '-' and matrix[r][c] != 'L' and matrix[r][c] != 'J':
                cnt += 1
        else:
            if cnt % 2 == 1:
                ans += 1

print(ans)
