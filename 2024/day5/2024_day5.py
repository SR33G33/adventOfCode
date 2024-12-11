import math

def parse_input():
    input_type = 1
    rules = []
    queues = []

    with open("input.txt") as file:
        for line in file:
            if(input_type == 1 and line != "\n"):
                line = line.split("|")
                rules.append((line[0].strip(), line[1].strip()))
            if(line == "\n"): input_type = 2
            if(input_type == 2 and line != "\n"):
                line = line.split(",")
                new_queue = []
                for element in range(len(line)):
                    new_queue.append(line[element].strip())
                queues.append(new_queue)
    return rules, queues  # Count the number of lights that are on

def check_queues(rules, queues, want):
    valid_queues = []
    valid = True
    for queue in queues:
        valid = True
        for element1 in range(len(queue)):
            for element2 in range(len(queue)):
                if(element1 < element2):
                    if((queue[element2], queue[element1]) in rules): 
                        temp = queue[element1]
                        queue[element1] = queue[element2]
                        queue[element2] = temp
                        valid = False
                elif(element2 < element1):
                    if((queue[element1], queue[element2]) in rules): 
                        temp = queue[element1]
                        queue[element1] = queue[element2]
                        queue[element2] = temp
                        valid = False
        # print(f"queue valid: {valid}  user wants: {want}")
        if(valid == want): valid_queues.append(queue)

    return valid_queues

 
def sum_middles(valid_queues):
    sum = 0
    for queue in valid_queues:
        sum += int(queue[int(len(queue)/2)])
    return sum

rules, queues = parse_input()
rules, queues2 = parse_input()

valid_queues = check_queues(rules, queues, True)
invalid_queues = check_queues(rules, queues2, False)
print(valid_queues)
print(invalid_queues)

print(f"The total sum for valid queues is: {sum_middles(valid_queues)}")
print(f"The total sum for corrected invalid queues is: {sum_middles(invalid_queues)}")

