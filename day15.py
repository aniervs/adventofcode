input_file = open("day15.in", "r")

def compute_hash(label):
    h = 0
    for c in label:
        h = (h + ord(c))*17 % 256
    return h

lst = input_file.readline().strip().split(",")

val = dict() # val[label]: value of the label
pos = dict() # pos[label]: position of the label in its corresponding box
box = [[] for _ in range(256)] # box[i]: list of labels in the i-th box
mark = [[] for _ in range(256)] # mark[i][j]: True if the j-th label in the i-th box is active, False otherwise
length = [0 for _ in range(256)] # length[i]: number of active labels in the i-th box

for operation in lst:
    if operation[-1] == "-":
        label = operation[:-1]
        h = compute_hash(label)
        if label not in pos or pos[label] is  None:
            continue 
        p = pos[label]
        mark[h][p] = False
        pos[label] = None 
        val[label] = None
        length[h] -= 1 
    else:
        label, value = operation.split("=")
        val[label] = int(value)
        if label in pos and pos[label] is not None:
            continue 
        h = compute_hash(label)
        box[h].append(label)
        mark[h].append(True)
        length[h] += 1
        pos[label] = len(box[h]) - 1

answer = 0
for h in range(256):
    if length[h] == 0:
        continue
    slot = 1
    for i in range(len(box[h])):
        if mark[h][i]:
            label = box[h][i]
            value = val[label]
            answer += value*slot*(h + 1)
            slot += 1
    
print(answer)

input_file.close()
