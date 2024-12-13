def parse_input():
    map = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                line_list = []
                for char in line:
                    if(char != "\n" and char != ""):
                        line_list.append(char)
                map.append(line_list)
    # print_map(map)
    # print("============")
    return map  

def get_same_antennas(antenna_row, antenna_col, map):
    antenna_type = map[antenna_row][antenna_col]
    antenna_map = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if(row != antenna_row and col != antenna_col and map[row][col] == antenna_type):
                antenna_map.append((row,col))
    return antenna_map

def in_range(point, map):
    return (point[0] >= 0 and point[0] < len(map) and point[1] >= 0 and point[1] < len(map[0]))

def get_opposite_position(row, col, point):
    diffX = point[0] - row
    diffY = point[1] - col

    return (point[0] + diffX, point[1] + diffY)

def print_map(map):
    for row in map:
        if(row):
            row_string = ""
            for col in row:
                row_string += col + ""
        print(row_string)

def get_num_antinodes(map, p2=False):
    unique_antenna_list = {}
    count = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if(map[row][col] != "." and map[row][col] != "#"):
                # print(f"Looking for: {map[row][col]}")
                antenna_list = get_same_antennas(row, col, map)
                for antenna in antenna_list:
                    if(in_range(get_opposite_position(row, col, antenna), map)): 
                        antinode = get_opposite_position(row, col, antenna)
                        unique_antenna_list[antinode] = 1
                        if(p2==True): 
                            unique_antenna_list[(row, col)] = 1
                            unique_antenna_list[antenna] = 1
                        if(map[antinode[0]][antinode[1]] == "."): map[antinode[0]][antinode[1]] = "#"
                    if(p2 == True):
                        current_point = (row, col)
                        current_antenna = antenna
                        antinode = get_opposite_position(current_point[0], current_point[1], current_antenna)

                        while(in_range(antinode, map)): 
                            # print(f"Continuing to: {antinode}")
                            unique_antenna_list[antinode] = 1
                            unique_antenna_list[current_point] = 1
                            unique_antenna_list[current_antenna] = 1
                            if(map[antinode[0]][antinode[1]] == "."): map[antinode[0]][antinode[1]] = "#"
                            current_point = current_antenna
                            current_antenna = antinode
                            antinode = get_opposite_position(current_point[0], current_point[1], antinode)



    
    # print_map(map)
    return len(unique_antenna_list.keys())

map = parse_input()

print(f"There are {get_num_antinodes(map, p2=True)} antinodes")

