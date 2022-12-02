DATA = open("solutions/resources/day1.txt", "r")

def task1(data):
    top_cals = 0
    curr_cals = 0
    elves = list()
    for cal in data:
        if cal == "\n":
            elves.append(curr_cals)
            if curr_cals > top_cals:
                top_cals = curr_cals
            curr_cals = 0
            continue
        curr_cals += int(cal)

    return [top_cals, elves]

def task2(data):
    top_cals = 0
    elves = task1(DATA)[1]

    top_three = list()
    for i in range(3):
        top_elf = 0
        for elf in elves:
            if int(elf) > top_elf:
                top_elf = int(elf)
        top_three.append(top_elf)
        elves.pop(elves.index(top_elf))

    return sum(top_three)

def main():
    print(task1(DATA))
    print(task2(DATA))
    DATA.close()

if __name__ == "__main__":
    main()