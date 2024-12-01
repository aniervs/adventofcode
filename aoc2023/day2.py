input_file = open("day2.in", "r")

answer = 0

def compute_power(game):
    game = game.strip()
    p = game.find(":")
    game = game[p+1:]
    sets = game.split(";")
    max_num = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for s in sets:
        for t in s.split(','):
            cnt, color = t.split(' ')[1:]
            max_num[color] = max(max_num[color], int(cnt))
    return max_num["red"] * max_num["green"] * max_num["blue"]

for idx, game in enumerate(input_file.readlines()):
    answer += compute_power(game)

print(answer)

input_file.close()