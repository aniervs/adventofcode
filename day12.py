input_file = open("day12.in", "r")

def solve(s, lst):
    si = s
    li = lst.copy()
    
    for _ in range(4):
        s += '?' + si 
        lst += li
        
    n, m = len(s), len(lst)
    
    s = "." + s
    lst = [0] + lst 
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n + 1):
        if s[i] != "#":
            dp[i][0] = 1
        else:
            break 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i] == '.' or s[i] == '?':
                dp[i][j] += dp[i-1][j]
            if (s[i] == '#' or s[i] == '?') and i >= lst[j] and s[i-lst[j]+1:i+1].count('.') == 0:
                if i - lst[j] == 0:
                    dp[i][j] += dp[i - lst[j]][j - 1]
                elif s[i - lst[j]] != '#':
                    dp[i][j] += dp[i-lst[j]-1][j-1]
        
    return dp[n][m]

ans = 0
for idx, line in enumerate(input_file.readlines()):
    s, l = line.strip().split(' ')
    l = list(map(int, l.split(',')))
    
    t = solve(s, l)

    ans += t 

print("Answer:", ans)

input_file.close()