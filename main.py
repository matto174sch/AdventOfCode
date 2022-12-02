from solutions import *

def main():
    data = open("solutions/resources/day1.txt", "r")
    print("Day 1:")
    print(f"> Solution Task 1: {day1.task1(data)[0]}")
    print(f"> Solution Task 2: {day1.task2()}")
    data.close()

    data = open("solutions/resources/day2.txt", "r")
    print("Day 2:")
    print(f"> Solution Day 2: {day2.task1(data)}")
    data.close()

    return None

if __name__ == "__main__":
    main()