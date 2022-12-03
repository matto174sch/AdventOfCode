from solutions import *

def main():
    data = open("solutions/resources/day1.txt", "r")
    print("Day 1:")
    print(f"> Solution Task 1: {day1.task1(data)[0]}")
    print(f"> Solution Task 2: {day1.task2()}")
    data.close()

    data = open("solutions/resources/day2.txt", "r")
    data2 = open("solutions/resources/day2.txt", "r")
    print("Day 2:")
    print(f"> Solution Task 1: {day2.task1(data)}")
    print(f"> Solution Task 2: {day2.task2(data2)}")
    data.close()
    data2.close()

    task1_3 = open("solutions/resources/day3.txt", "r")
    print("Day 3:")
    print(f"> Solution Task 1: {day3.task1(task1_3)}")
    #print(f"> Solution Task 2: {day2.task2(data2)}")
    task1_3.close()


    return None

if __name__ == "__main__":
    main()