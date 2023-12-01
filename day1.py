input_file = open("day1.in", "r")

def process(s: str) -> int:
    min_pos = None 
    first_dig = None 
    max_pos = None
    last_dig = None
    
    for idx, number in zip(range(1, 10), ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        first_ocurrence = s.find(number)
        last_ocurrence = s[::-1].find(number[::-1])
        if first_ocurrence != -1:
            if min_pos is None or first_ocurrence < min_pos:
                min_pos = first_ocurrence
                first_dig = idx
        if last_ocurrence != -1:
            if max_pos is None or last_ocurrence < max_pos:
                max_pos = last_ocurrence
                last_dig = idx
    
    for idx, c in enumerate(s):
        if c.isnumeric():
            if min_pos is None or idx < min_pos:
                min_pos = idx
                first_dig = int(c)
            break 
    for idx, c in enumerate(s[::-1]):
        if c.isnumeric():
            if max_pos is None or idx < max_pos:
                max_pos = idx
                last_dig = int(c)
            break

    return first_dig*10 + last_dig
        

answer = 0
for line in input_file.readlines():
    answer += process(line)
        
print(answer)

input_file.close()
