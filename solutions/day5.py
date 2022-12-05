import re
DATA = open("solutions/resources/day5.txt", "r")

def task1(data):
    res = get_inst_dict(data)
    instructions = res[0]
    stacks_dict = res[1]

    for instruction in instructions:
        move_crates1(instruction, stacks_dict)
    
    return top_stacks(stacks_dict)
    
def get_inst_dict(data):
    stacks = list()
    instructions = list()
    stacks_dict = {}
    bool_inst = 0
    for line in data.readlines():
        if bool_inst:
            instructions.append(line.rstrip())
            continue
        if line == "\n":
            bool_inst = 1
            continue
        stacks.append(line[:-1])

    for i in range(9):
        stacks_dict[i+1] = []
        for stack in reversed(stacks[:-1]):
            if i == 0:
                stacks_dict[i+1].append(stack[i:3])
            elif i == 8:
                stacks_dict[i+1].append(stack[i+i*3:])
            else: 
                stacks_dict[i+1].append(stack[i+i*3:i+i*3+3])
    
    for value in stacks_dict.values():
        while "   " in value:
            value.remove("   ")
    
    return [instructions, stacks_dict]


def move_crates1(instruction, stacks_dict):
    numbers = re.findall('\d+', instruction)
    quantity = int(numbers[0])
    from_stack = int(numbers[1])
    to_stack = int(numbers[-1])

    for _ in range(quantity):
        stacks_dict[to_stack].append(stacks_dict[from_stack].pop())

    return stacks_dict

def top_stacks(stacks_dict):
    top_values = ""
    for stack in stacks_dict.values():
        try:
            top_values += stack[-1][1]
        except:
            continue

    return top_values

def move_crates2(instruction, stacks_dict):
    numbers = re.findall('\d+', instruction)
    quantity = int(numbers[0])
    from_stack = int(numbers[1])
    to_stack = int(numbers[-1])

    stacks_dict[to_stack] += stacks_dict[from_stack][len(stacks_dict[from_stack])-quantity:]
    stacks_dict[from_stack] = stacks_dict[from_stack][:len(stacks_dict[from_stack])-quantity]

    return stacks_dict

def task2(data):
    res = get_inst_dict(data)
    instructions = res[0]
    stacks_dict = res[1]

    for instruction in instructions:
        move_crates2(instruction, stacks_dict)
    
    return top_stacks(stacks_dict)

def main():
    print(task1(DATA))
    print(task2(DATA))
    DATA.close()
    return

if __name__ == "__main__":
    main()
