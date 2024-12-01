input_file = open("day11.in", "r")

matrix = []
for line in input_file.readlines():
    line = list(line.strip())
    matrix.append(line)

n, m = len(matrix), len(matrix[0])

count_row = [0] * n
count_col = [0] * m

for r in range(n):
    if matrix[r].count('.') == m:
        count_row[r] += 1
    if r > 0:
        count_row[r] += count_row[r - 1]

for c in range(m):
    col = [matrix[r][c] for r in range(n)]
    if col.count('.') == n:
        count_col[c] += 1
    if c > 0:
        count_col[c] += count_col[c - 1]

def get_row(l, r):
    if l > r:
        l, r = r, l
    res = count_row[r]
    if l > 0:
        res -= count_row[l - 1]
    return res
def get_col(l, r):
    if l > r:
        l, r = r, l
    res = count_col[r]
    if l > 0:
        res -= count_col[l - 1]
    return res

def dist(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1]) + (get_row(point1[0], point2[0]) + get_col(point1[1], point2[1])) * (int(1e6 - 1))

points = [(r, c) for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == '#']

ans = 0
for p1 in range(len(points)):
    for p2 in range(p1 + 1, len(points)):
        # print(points[p1], points[p2], '--->', dist(points[p1], points[p2]))
        ans += dist(points[p1], points[p2])

print(n, m)
print(ans)

input_file.close()