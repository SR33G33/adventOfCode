import re

def parse_input():
    with open("input.txt") as file:
        for line in file:
            if(line):
                return line

def scan_corrupted(corrupt_memory):
    sum = 0
    mult_pattern = r"mul\([0-9]+,[0-9]+\)" # Matches one or more digits
    multiplications = re.findall(mult_pattern, corrupt_memory)

    # print(multiplications)
    for operation in multiplications:
        numbers_pattern = r"[0-9]+,[0-9]+"
        numbers = re.findall(numbers_pattern, operation)
        numbers = (numbers[0]).split(",")
        sum += int(numbers[0]) * int(numbers[1])    
    return sum

def scan_corrupted_do(corrupt_memory):
    sum = 0

    mult_pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" # Matches one or more digits
    multiplications = re.findall(mult_pattern, corrupt_memory)
    # print(multiplications)

    # print(multiplications)
    do = True
    for operation in multiplications:
        if(operation == "do()"): do = True
        elif(operation == "don't()"): do = False
        if(do):
            numbers_pattern = r"[0-9]+,[0-9]+"
            numbers = re.findall(numbers_pattern, operation)
            if(numbers):
                numbers = (numbers[0]).split(",")
                sum += int(numbers[0]) * int(numbers[1])    
    return sum

corrupt_memory = parse_input()
print(f"The sum of the corrupted memory is: {scan_corrupted(corrupt_memory)}")
print(f"The sum of the corrupted memory with do() is: {scan_corrupted_do(corrupt_memory)}")

