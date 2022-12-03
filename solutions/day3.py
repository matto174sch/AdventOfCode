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

    letters = list(string.ascii_letters)
    sum_prio = 0
    for share in shares:
        sum_prio += letters.index(share) + 1

    return sum_prio

def main():
    print(task1(DATA))
    DATA.close()
    return

if __name__ == "__main__":
    main()