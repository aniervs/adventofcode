def preprocess_line(line):
    p = line.find(":")
    line = line[p+1:].strip().split(" ")
    res = "".join([x for x in line if x.isnumeric()])
    return [int(res)]

input_file = open("day6.in", "r")

durations = preprocess_line(input_file.readline())
distances = preprocess_line(input_file.readline())

print(f"Durations: {durations}")
print(f"Distances: {distances}")

answer = 1

for d, c in zip(durations, distances):
    l, r = 0, d
    while l < r:
        mid = (l + r) // 2
        if (d - mid) * mid <= c:
            l = mid + 1
        else:
            r = mid
    L = l 
    l, r = 0, d 
    while l < r:
        mid = (l + r + 1) // 2
        if (d - mid) * mid <= c:
            r = mid - 1
        else:
            l = mid
    R = r
    
    answer *= (R - L + 1)

print(answer)

input_file.close()