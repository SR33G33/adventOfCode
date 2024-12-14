def parse_input():
    map = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                line_list = []
                for char in line:
                    if(char != "\n" and char != ""):
                        if(char.isdigit()):
                            line_list.append(int(char))
                        else: line_list.append((char))

                map.append(line_list)
    print_map(map)
    # print("============")
    return map  

def get_trail_heads(trail_map):
    trail_heads_list = []
    for row in range(len(trail_map)):
        for col in range(len(trail_map[row])):
            if(trail_map[row][col] == 0):
                trail_heads_list.append((row, col))
    return trail_heads_list

def in_range(point, map):
    return (point[0] >= 0 and point[0] < len(map) and point[1] >= 0 and point[1] < len(map[0]))

def get_trail_score(trail_point, trail_map, trail_ends):
    current_position = trail_map[trail_point[0]][trail_point[1]]
    score = 0
    if(current_position == 9): 
        trail_ends[trail_point] = 1
        score += 1
        return trail_ends, score

    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    for i in range(len(directions)):
        direction = directions[i]
        new_point = (trail_point[0] + direction[0], trail_point[1] + direction[1])
        if(in_range(new_point, trail_map)):
            new_position = trail_map[new_point[0]][new_point[1]]
            # print(f"Checking Point {new_point[0]},{new_point[1]} with value {new_position}")
            if(new_position == current_position + 1):
                new_ends_list, new_score = get_trail_score(new_point, trail_map, trail_ends)
                trail_ends = trail_ends | new_ends_list
                score += new_score
    return trail_ends, score

def get_map_score(trail_map):
    trail_heads_list = get_trail_heads(trail_map)
    print(trail_heads_list)
    score = 0
    distinct_score = 0

    for trail_head in trail_heads_list:
        trail_ends = {}
        trail_ends, distinct_num = get_trail_score(trail_head, trail_map, trail_ends)
        trail_score = len(trail_ends.keys())
        print(f"Trail Score: {trail_score}")
        score += trail_score
        distinct_score += distinct_num

    return score, distinct_score

def print_map(map):
    for row in map:
        if(row):
            row_string = ""
            for col in row:
                row_string += str(col) + ""
        print(row_string)

trail_map = parse_input()
trail_score, distinct_trail_score = get_map_score(trail_map)

print(f"The Map has a score of {trail_score} with {distinct_trail_score} distinct score")


