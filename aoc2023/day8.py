from math import gcd, lcm
input_file = open("day8.in", "r")

instructions = input_file.readline().strip()
input_file.readline()

graph = {}
start_node = []

for line in input_file.readlines():
    line = line.strip()
    p = line.find("=")
    node = line[:p-1]
    if node[-1] == "A":
        start_node.append(node)
    line = line[p + 3:-1]
    l, r = line.split(", ")
    graph[node] = {"L": l, "R": r}

def process_node(node):
    first_time = dict()
    dst = 0
    z_node, z_dst = None, None 
    while True:
        if (node, dst % len(instructions)) in first_time:
            break 
        if node[-1] == "Z":
            z_node, z_dst = node, dst
        first_time[(node, dst % len(instructions))] = dst
        node = graph[node][instructions[dst % len(instructions)]]
        dst += 1
    
    cycle_length = dst - first_time[(node, dst % len(instructions))]
    return z_dst, cycle_length

def isprime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True 

nums = []

for node in start_node:
    z_dst, cycle_length = process_node(node)
    print("Starting node: {}, Cycle length: {}, Distance to Z: {}".format(node, cycle_length, z_dst))
    nums.append(cycle_length)
  

N = 1
for n in nums:
    N = lcm(n, N)

print(N)    
        
input_file.close()