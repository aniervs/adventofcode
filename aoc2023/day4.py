def compute_matches(card):
    p = card.find(":")
    card = card[p + 1:]
    win, nums = card.split("|")
    win = set(win.strip().split(" "))
    if " " in win:
        win.remove(" ")
    nums = nums.strip().split(" ")
    k = 0
    for x in nums:
        if x.isnumeric() and x in win:
            k += 1
    return k 



def main():
    input_file = open("day4.in", "r")
    
    lines = input_file.readlines()
    n = len(lines)
    
    cnt = [1] * n
    
    for idx, card in enumerate(lines):
        k = compute_matches(card)
        for i in range(1, k + 1):
            if idx + i >= n:
                break 
            cnt[idx + i] += cnt[idx]
        
    print(sum(cnt))
        
    input_file.close()
    
if __name__ == "__main__":
    main()
    

