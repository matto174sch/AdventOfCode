DATA = open("solutions/resources/day2.txt", "r")
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# A = ROCK, B = PAPER, C = SCISSORS
# X = ROCK, Y = PAPER, Z = SCISSORS
# IF A: X => DRAW, Y => WIN, Z => LOSS
# IF B: X => LOSS, Y => DRAW, Z => WIN
# IF C: X => WIN, Y => LOSS, Z => WIN

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

def main():
    print(task1(DATA))
    DATA.close()

if __name__ == "__main__":
    main()