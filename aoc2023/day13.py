input_file = open("day13.in", "r")

def get_error(a, b):
    res = 0
    for ra, rb in zip(a, b):
        for ca, cb in zip(ra, rb):
            if ca != cb:
                res += 1
    return res 

def process(matrix):
    n, m = len(matrix), len(matrix[0])
    
    # horizontal
    for r in range(n-1):
        above = matrix[:r+1][::-1]
        below = matrix[r+1:]
        if r+1 <= n-r-1:
            if get_error(above, below[:r+1]) == 1:
                return "horizontal", r
        elif get_error(below, above[:n-r-1]) == 1:
            return "horizontal", r

    # vertical
    for c in range(m-1):       
        left = [[matrix[r][i] for r in range(n)] for i in range(c+1)][::-1]
        right = [[matrix[r][i] for r in range(n)] for i in range(c+1, m)]
        
        if c+1 <= m-c-1:
            if get_error(left, right[:c+1]) == 1:
                return "vertical", c
        elif get_error(right, left[:m-c-1]) == 1:
            return "vertical", c
    
    return None, None 

ans = 0
matrix = []
for line in input_file.readlines():
    line = line.strip()
    if line == "":
        ot, oidx = process(matrix)
        if ot == "horizontal":
            ans += (oidx + 1) * 100
        else:
            ans += (oidx + 1)
        matrix = []
        continue 
    matrix.append(list(line))

print(ans)
input_file.close()