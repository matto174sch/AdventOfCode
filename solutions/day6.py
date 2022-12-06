DATA = open("solutions/resources/day6.txt", "r")

def task1(data):
    input_str = data.read()
    seen = [input_str[0], input_str[1], input_str[2]]
    i = 3 
    for char in input_str[3:]:
        if char not in list(set(seen)) and len(list(set(seen))) == 3:
            return i + 1

        del seen[0]
        seen.append(char)
        i += 1

    return 

def task2(data):
    input_str = data.read()
    seen = list()
    for i in range(13):
        seen.append(input_str[i])
    i = 13 
    for char in input_str[13:]:
        if char not in list(set(seen)) and len(list(set(seen))) == 13:
            return i + 1

        del seen[0]
        seen.append(char)
        i += 1

    return

def main():
    print(task1(DATA))
    print(task2(DATA))
    DATA.close()
    return

if __name__ == "__main__":
    main()
