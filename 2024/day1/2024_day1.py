def parse_input():
    loc_ID_list1 = []
    loc_ID_list2 = []

    with open("input.txt") as file:
        for line in file:
            line = line.split("   ")
            loc_ID_list1.append(int(line[0].strip()))
            loc_ID_list2.append(int(line[1].strip()))

    loc_ID_list1.sort()
    loc_ID_list2.sort()

    return loc_ID_list1, loc_ID_list2  # Count the number of lights that are on

def calculate_difference(list1, list2):
    total_diff = 0
    for index in range(len(list1)):
        total_diff += abs(list1[index]-list2[index])
    return total_diff

def calculate_similarity(list1, list2):
    total_similarity = 0
    for index in range(len(list1)):
        total_similarity += list1[index] * list2.count(list1[index])
    return total_similarity

id_list1, id_list2 = parse_input()
print(f"The total distance is: {calculate_difference(id_list1, id_list2)}")
print(f"The total similarity is: {calculate_similarity(id_list1, id_list2)}")
