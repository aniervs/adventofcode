from collections import deque

moves = [(0, 1), (1, 0), (0, -1),  (-1, 0)]
moves_maps = ['R', 'D', 'L', 'U']


def main():

    input_file = open("day18.in", "r")

    points = [(0, 0)]
    r, c = 0, 0

    for line in input_file:
        info = line.strip().split(" ")[-1][2:-1]
        n_steps = int(info[:-1], 16)
        dir_idx = int(info[-1])
        n_steps = int(n_steps)
        
        r, c = r + moves[dir_idx][0] * n_steps, c + moves[dir_idx][1] * n_steps
        points.append((r, c))
        
    
    min_x = min(x for _, x in points)
    min_y = min(y for y, _ in points)
    
    points = [(y - min_y, x - min_x) for y, x in points]
    
    min_point = min(points)
    id_min = points.index(min_point)
    points = points[:-1]
    points = points[id_min:] + points[:id_min+1]
        
    
    new_points = [min_point]
    for i in range(1, len(points) - 1):
        r0, c0 = points[i-1]
        r1, c1 = points[i]
        r2, c2 = points[i+1]

        if r0 == r1:
            # option1: right up
            if c0 < c1 and r1 > r2:
                pass 
            # option2: right down
            elif c0 < c1 and r1 < r2:
                c1 += 1
            # option3: left up
            elif c0 > c1 and r1 > r2:
                r1 += 1
            # option4: left down
            elif c0 > c1 and r1 < r2:
                r1 += 1
                c1 += 1
            else:
                raise Exception("Invalid")
        elif c0 == c1:
            # option1: up right
            if r0 > r1 and c1 < c2:
                pass
            # option2: up left
            elif r0 > r1 and c1 > c2:
                r1 += 1
            # option3: down right
            elif r0 < r1 and c1 < c2:
                c1 += 1
            # option4: down left
            elif r0 < r1 and c1 > c2:
                r1 += 1
                c1 += 1
            else:
                raise Exception("Invalid")
        else:
            raise Exception("Invalid")
        
        new_points.append((r1, c1))
    
    ans = 0
    

    max_y = max(y for y, _ in new_points)
    
    for i in range(len(new_points)):
        r, c = new_points[i]
        nr, nc = new_points[(i+1) % len(new_points)]
        
        if r == nr:
            ans += (nc - c) * (max_y - r)
        
    print(ans)
    
    input_file.close()
    
if __name__ == "__main__":
    main()