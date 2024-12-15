from collections import defaultdict

def parse_input():
    map = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                line = line.split(" ")
    print(line)
    return line 

memory = {}

def blink(stones_list):
    output_list = []
    for stone_i in range(len(stones_list)):
        stone = stones_list[stone_i]
        if((stone) == "0"): output_list.append("1")
        elif(len(stone) % 2 == 0):
            output_list.append(str(int(stone[0:int(len(stone)/2)])))
            output_list.append(str(int(stone[int(len(stone)/2):])))
        else:
            output_list.append(str(int(stone)*2024))
    return output_list

def num_stones_after_blinks(stones_list, num_blinks):
    for i in range(num_blinks):
        # print(f"Blink #{i}")
        stones_list = blink(stones_list)
        # print(stones_list)

    return len(stones_list)

stones_init = parse_input()
num_blinks = 25
num_blinks2 = 75


print(f"There are {num_stones_after_blinks(stones_init, num_blinks)} after {num_blinks} blinks")
print(f"There are {num_stones_after_blinks(stones_init, num_blinks2)} after {num_blinks2} blinks")



