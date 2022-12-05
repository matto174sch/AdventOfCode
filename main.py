from solutions import *

def main():
    data = open("solutions/resources/day1.txt", "r")
    print("Day 1:")
    print(f"> Solution Task 1: {day1.task1(data)[0]}")
    print(f"> Solution Task 2: {day1.task2()}")
    data.close()

    data = open("solutions/resources/day2.txt", "r")
    data2 = open("solutions/resources/day2.txt", "r")
    print("\nDay 2:")
    print(f"> Solution Task 1: {day2.task1(data)}")
    print(f"> Solution Task 2: {day2.task2(data2)}")
    data.close()
    data2.close()

    task13 = open("solutions/resources/day3.txt", "r")
    print("\nDay 3:")
    print(f"> Solution Task 1: {day3.task1(task13)}")
    task13.close()
    task23 = open("solutions/resources/day3.txt", "r")
    print(f"> Solution Task 2: {day3.task2(task23)}")
    task23.close()

    task14 = open("solutions/resources/day4.txt", "r")
    print("\nDay 4:")
    print(f"> Solution Task 1: {day4.task1(task14)}")
    task14.close()
    task24 = open("solutions/resources/day4.txt", "r")
    print(f"> Solution Task 2: {day4.task2(task24)}")
    task24.close()

    task15 = open("solutions/resources/day5.txt", "r")
    print("\nDay 5:")
    print(f"> Solution Task 1: {day5.task1(task15)}")
    task15.close()
    task25 = open("solutions/resources/day5.txt", "r")
    print(f"> Solution Task 2: {day5.task2(task25)}")
    task25.close()
    return None

if __name__ == "__main__":
    main()