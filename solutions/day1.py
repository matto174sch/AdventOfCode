def solution_day1():
	data = open("solutions/resources/day1/day1.txt", "r")

	top_cals = 0
	curr_cals = 0
	for cal in data:
		cal.rstrip()
		if cal == "\n":
			if curr_cals > top_cals:
				top_cals = curr_cals
			curr_cals = 0
			continue
		curr_cals += int(cal)

	data.close()

	return top_cals

def main():
	print(solution_day1())

if __name__ == "__main__":
	main()