DATA = open("solutions/resources/day2.txt", "r")
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# A = ROCK, B = PAPER, C = SCISSORS
# X = ROCK, Y = PAPER, Z = SCISSORS
# IF A: X => DRAW, Y => WIN, Z => LOSS
# IF B: X => LOSS, Y => DRAW, Z => WIN
# IF C: X => WIN, Y => LOSS, Z => DRAW

def calc_round_outcome(line):
    # line = [opponent, you]
    opponent = line[0]
    you = line[1]
    if opponent == "A":
        if you == "X":
            # draw
            return 3
        if you == "Y":
            # win
            return 6
        if you == "Z":
            #loss
            return 0

    if opponent == "B":
        if you == "X":
            # loss
            return 0
        if you == "Y":
            # draw
            return 3
        if you == "Z":
            # win
            return 6

    if opponent == "C":
        if you == "X":
            # win
            return 6
        if you == "Y":
            # loss
            return 0
        if you == "Z":
            # draw
            return 3

    return "error"

def calc_round_score(line):
    you = line[1]
    if you == "X":
        return 1
    
    if you == "Y":
        return 2

    if you == "Z":
        return 3

    return "error"

def task1(data):
    total_score = 0
    for line in data:
        total_score += calc_round_outcome(line.rstrip().split(" ")) + calc_round_score(line.rstrip().split(" "))

    return total_score

def cal_outcome_task2(line):
    opp = line[0]
    you = line[1]

    # IF YOU = X: LOSE!
    # IF YOU = Y: DRAW!
    # IF YOU = Z: WIN!

    if you == "X":
        if opp == "A":
            return [0, "Z"]

        if opp == "B":
            return [0, "X"]

        if opp == "C":
            return [0, "Y"]

    if you == "Y":
        if opp == "A":
            return [3, "X"]

        if opp == "B":
            return [3, "Y"]

        if opp == "C":
            return [3, "Z"]
    
    if you == "Z":
        if opp == "A":
            return [6, "Y"]

        if opp == "B":
            return [6, "Z"]

        if opp == "C":
            return [6, "X"]
    
    return "error"

def calc_round_score_task2(token):
    if token == "X":
        return 1
    
    if token == "Y":
        return 2

    if token == "Z":
        return 3

    return "error" 

def task2(data):
    total_score = 0
    for line in data:
        res = cal_outcome_task2(line.rstrip().split(" "))
        total_score += res[0] + calc_round_score_task2(res[1])

    return total_score

def main():
    print(task1(DATA))
    print(task2(DATA))
    DATA.close()

if __name__ == "__main__":
    main()