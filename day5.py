MAXX = 4259440029
def compute_intersection(l1, r1, l2, r2):
    L, R = max(l1, l2), min(r1, r2)
    if L > R:
        return None, None 
    return L, R

def complete(blocks):
    blocks.sort()
    new_blocks = []
    for l, r, o_l, o_r in blocks:
        if len(new_blocks) > 0 and new_blocks[-1] == (l, r, o_l, o_r):
            continue
        new_blocks.append((l, r, o_l, o_r))
    return new_blocks
    

def main():
    input_file = open('day5.in', 'r')
    
    seeds = list(map(int, input_file.readline().strip()[7:].split(' ')))
    n = len(seeds)
    initial_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, n, 2)]
    
    layers = [[] for _ in range(7)]
    # empty line
    input_file.readline()
    
    for step in range(7):
        input_file.readline() # name of the layer
        while True:
            line = input_file.readline().strip()
            if line == "":
                break
            dst_l, src_l, length = map(int, line.split(' '))
            layers[step].append((src_l, src_l+length-1, dst_l, dst_l+length-1))
            
        
    blocks = [(l2, r2, l2, r2) for l1, r1, l2, r2 in layers[-1]]
    blocks.sort()
    new_blocks = []
    last_position = -1
    for l, r, _, _ in blocks:
        if l > last_position + 1:
            new_blocks.append((last_position + 1, l - 1, last_position + 1, l - 1))
        new_blocks.append((l, r, l, r))
        last_position = r
    if last_position < MAXX:
        new_blocks.append((last_position + 1, MAXX, last_position + 1, MAXX))
    blocks = new_blocks.copy()
    del new_blocks
    
    for layer in layers[-1::-1]:
        new_blocks = []
        for block in blocks:
            tmp_blocks = [block]
            i = 0
            while i < len(tmp_blocks):
                a, b, o_a, o_b = tmp_blocks[i]
                assert a <= b
                assert o_a <= o_b
                assert o_b - o_a == b - a,  f"Offsets are not equal {layer}"
                found_intersection = False
                for l1, r1, l2, r2 in layer:
                    l, r = compute_intersection(l2, r2, a, b)
                    if l is not None:
                        found_intersection = True
                        new_blocks.append((l1 + (l-l2), r1-(r2-r), o_a+(l-a), o_b - (b-r)))
                        if l > a:
                            tmp_blocks.append((a, l-1, o_a, o_a + (l-1-a)))
                        if r < b:
                            tmp_blocks.append((r+1, b, o_a + (r+1-a), o_b))
                if not found_intersection:
                    new_blocks.append((a, b, o_a, o_b))
                i += 1
        blocks = complete(new_blocks)
    
    ans = None 
    for l, r, o_l, o_r in blocks:
        for a,b in initial_ranges:
            L, R = compute_intersection(l, r, a, b)
            if L is not None:
                if ans is None:
                    ans = L + o_l
                ans = min(ans, L + o_l - l)
    print(ans)
    
    input_file.close()


if __name__ == '__main__':
    main()