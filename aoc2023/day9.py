input_file = open("day9.in", "r")

def solve(seq):
    if seq.count(0) == len(seq):
        return 0
    return seq[0] - solve([seq[i+1]-seq[i] for i in range(len(seq)-1)])
    


ans = 0
for line in input_file.readlines():
    seq = list(map(int, line.strip().split()))
    ans += solve(seq)
print(ans)
input_file.close()