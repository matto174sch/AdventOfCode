DATA = open("solutions/resources/day3.txt", "r")

def task1(data):
    output = 0
    for pair in data:
        first, second = pair.rstrip().split(",")[0], pair.rstrip().split(",")[1]
        frange1, frange2 = first.split("-")[0], first.split("-")[1]
        srange1, srange2 = second.split("-")[0], second.split("-")[1]

        first_range = list(range(int(frange1), int(frange2) + 1))
        second_range = list(range(int(srange1), int(srange2) + 1))

        shares = list()
        for frst in first_range:
            if frst in second_range:
                shares.append(frst)

        shares2 = list()
        for snd in second_range:
            if snd in first_range:
                shares2.append(snd)
        
        if shares == first_range or shares2 == second_range:
            output += 1

    return output

def task2(data):
    output = 0

    for pair in data:
        first, second = pair.rstrip().split(",")[0], pair.rstrip().split(",")[1]
        frange1, frange2 = first.split("-")[0], first.split("-")[1]
        srange1, srange2 = second.split("-")[0], second.split("-")[1]

        first_range = range(int(frange1), int(frange2) + 1)
        second_range = range(int(srange1), int(srange2) + 1)
        
        if list(set(first_range) & set(second_range)):
            output += 1

    return output

def main():
    print(task1(DATA))
    print(task2(DATA))
    DATA.close()
    return

if __name__ == "__main__":
    main()
