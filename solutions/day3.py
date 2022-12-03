import string
DATA = open("solutions/resources/day3.txt", "r")

def task1(data):
    first_comp = list()
    second_comp = list()
    for rucksack in data:
        leng = int(len(rucksack.rstrip())/2)
        first_comp.append(rucksack[:leng])
        second_comp.append(rucksack[leng:])
    
    shares = list()
    for i in range(len(first_comp)):
        seen = list()
        for item in first_comp[i]:
            if item in second_comp[i] and item not in seen:
                shares.append(item)
                seen.append(item)

    return get_sum_prios(shares)

def get_sum_prios(shares):
    letters = list(string.ascii_letters)
    sum_prio = 0
    for share in shares:
        sum_prio += letters.index(share) + 1

    return sum_prio

def task2(data):
    i = 0
    j = 1 
    groups = {}
    group = list()
    for rucksack in data:
        group.append(rucksack.rstrip())
        i += 1
        if i == 3:
            groups[j] = group
            group = list()
            i = 0
            j += 1

    shares = list()
    for group in groups.values():
        for bag in group:
            seen = list()
            for item in bag:
                if item in group[1] and item in group[2] and item not in seen:
                    seen.append(item)
                    shares.append(item)
            break

    return get_sum_prios(shares)


def main():
    print(task1(DATA))
    print(task2(DATA))
    DATA.close()
    return

if __name__ == "__main__":
    main()