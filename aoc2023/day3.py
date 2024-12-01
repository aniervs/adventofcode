
input_file = open("day3.in", "r")

matrix = [line.strip() for line in input_file.readlines()]

n = len(matrix)
m = len(matrix[0])

answer = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            candidates = set()
            for new_i in range(i - 1, i + 2):
                for new_j in range(j - 1, j + 2):
                    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m or (new_i == i and new_j == j) or not matrix[new_i][new_j].isnumeric():
                        continue
                    l, r = new_j, new_j
                    while l > 0 and matrix[new_i][l - 1].isnumeric():
                        l -= 1
                    while r + 1 < m and matrix[new_i][r + 1].isnumeric():
                        r += 1
                    candidates.add((new_i, l, r))
            
            if len(candidates) == 2:
                candidates = list(candidates)
                row1, l1, r1 = candidates[0]
                row2, l2, r2 = candidates[1]
                answer += int(matrix[row1][l1:r1 + 1]) * int(matrix[row2][l2:r2 + 1])

print(answer)
input_file.close()
