input_file = open("day7.in", "r")

kinds = ["J"] + list(range(2, 10)) + ["T", "Q", "K", "A"]
kind_rank = {str(kinds[i]): i for i in range(len(kinds))}
decode = lambda hand: "".join([str(kinds[c]) for c in hand])

hands = []

def compute_rank_hand(hand):
    old_hand = hand.copy()
    answer = 0 # high card
    for new_val_joker in range(1, len(kinds)):
        hand = old_hand.copy()
        for i in range(len(hand)):
            if hand[i] == 0:
                hand[i] = new_val_joker
        hand.sort()
        # five of a kind
        if hand[0] == hand[-1]:
            answer = max(answer, 6)
            continue 
        # four of a kind
        if hand[0] == hand[-2] or hand[1] == hand[-1]:
            answer = max(answer, 5)
            continue 
        # full house
        if (hand[0] == hand[1] and hand[2] == hand[-1]) or (hand[0] == hand[2] and hand[3] == hand[-1]):
            answer = max(answer, 4)
            continue
        # three of a kind
        if hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
            answer = max(answer, 3)
            continue 
        # two pairs
        if (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[1] == hand[2] and hand[3] == hand[4]):
            answer = max(answer, 2)
            continue 
        # one pair
        if hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
            answer = max(answer, 1)
            continue 
            
    return answer 
    

for line in input_file:
    hand, bid = line.strip().split(" ")
    bid = int(bid)
    hand = [kind_rank[c] for c in hand]
    hands.append((compute_rank_hand(hand.copy()), hand, bid))

hands.sort()

ans = 0
for idx, (rank, hand, bid) in enumerate(hands):
    ans += (idx + 1) * bid
print(ans)

input_file.close()