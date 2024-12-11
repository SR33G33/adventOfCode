import math
import copy

def parse_input():
    map = []
    guard_pos = (0,0)

    with open("input.txt") as file:
        row_num = 0
        for line in file:
            row = []
            for col in line:
                if(col.strip() != ""):
                    row.append(col.strip())
                    if(col.strip() == "^"):
                        guard_pos = (row_num, row.index(col))
            map.append(row)
            row_num += 1
    # print_map(map)
    return map, guard_pos  # Count the number of lights that are on

def next_position(guard_pos, dir):
    directions = {"up":(-1,0), "right":(0,1), "down":(1,0), "left":(0,-1)}
    # dir = directions[dir]
    return (guard_pos[0] + dir[0], guard_pos[1] + dir[1])

def is_in_range(position, map):
    return (position[0] >= 0 and position[0] < len(map) and position[1] >= 0 and position[1] < len(map[0]))

def index_of_dir(dir, directions):
    # print(directions.keys())
    for key in range(len(directions.keys())):
        if(dir == directions[list(directions.keys())[key]]): return key

def move_guard(map, guard_pos, dir):
    directions = {"up":(-1,0), "right":(0,1), "down":(1,0), "left":(0,-1)}
    in_range = True
    next_pos = next_position(guard_pos, dir)
    if(is_in_range(next_pos, map)):
        if(map[next_pos[0]][next_pos[1]] == "#"):
            dir_index = index_of_dir(dir, directions)
            if(dir_index >= 3): 
                dir_index = 0
            else: 
                dir_index += 1
            print(dir_index)
            dir = directions[list(directions.keys())[dir_index]]
            print("Direction Change")
        else:
            map[next_pos[0]][next_pos[1]] = "^"
            if((dir[0]) == 1): dir_char = "d"                
            elif((dir[0]) == -1): dir_char = "u"
            elif((dir[1]) == 1): dir_char = "r"
            elif((dir[1]) == -1): dir_char = "l"

            map[guard_pos[0]][guard_pos[1]] = dir_char
            guard_pos = next_pos
    else:
        in_range = False
        if((dir[0]) == 1): dir_char = "d"                
        elif((dir[0]) == -1): dir_char = "u"
        elif((dir[1]) == 1): dir_char = "r"
        elif((dir[1]) == -1): dir_char = "l"

        map[guard_pos[0]][guard_pos[1]] = dir_char
        return in_range, map, guard_pos, dir

def calc_path(map, guard_pos):
    path_map = map.copy()
    guard_in_range = True
    directions = {"up":(-1,0), "right":(0,1), "down":(1,0), "left":(0,-1)}
    dir = directions["up"]

    while(guard_in_range):
        guard_in_range, path_map, guard_pos, dir = move_guard(path_map, guard_pos, dir)
        # print_map(path_map)
    return path_map

def count_paths(path_map):
    count = 0
    for row in path_map:
        count += row.count("X")
    return count

def print_map(map):
    for row in map:
        row_string = ""
        for col in row:
            row_string += col + ""
        print(row_string)

def move_guard_loop(map, guard_pos, dir):
    directions = {"up":(-1,0), "right":(0,1), "down":(1,0), "left":(0,-1)}
    in_range = True
    loop = False
    next_pos = next_position(guard_pos, dir)
    if(is_in_range(next_pos, map)):
        # if(map[next_pos[0]][next_pos[1]] == "u"):
        #     if(abs(dir[1]) == -1): 
        #         loop = True
        #         print("=============")
        #         print_map(map)
        #         return loop, in_range, map, guard_pos, dir
        # elif(map[next_pos[0]][next_pos[1]] == "d"):
        #     if(abs(dir[1]) == 1): 
        #         loop = True
        #         print("=============")
        #         print_map(map)
        #         return loop, in_range, map, guard_pos, dir
        # elif(map[next_pos[0]][next_pos[1]] == "l"):
        #     if(abs(dir[0]) == -1): 
        #         print("=============")
        #         print_map(map)
        #         loop = True
        #         return loop, in_range, map, guard_pos, dir
        # elif(map[next_pos[0]][next_pos[1]] == "r"):
        #     if(abs(dir[0]) == 1): 
        #         print("=============")
        #         print_map(map)
        #         loop = True
        #         return loop, in_range, map, guard_pos, dir
        if(map[guard_pos[0]][guard_pos[1]] == "+"):
            if((dir[0]) == 1): dir_char = "d"                
            elif((dir[0]) == -1): dir_char = "u"
            elif((dir[1]) == 1): dir_char = "r"
            elif((dir[1]) == -1): dir_char = "l"

            if map[next_pos[0]][next_pos[1]] == dir_char:
                loop = True
                return loop, in_range, map, guard_pos, dir
        if(map[next_pos[0]][next_pos[1]] == "#" or map[next_pos[0]][next_pos[1]] == "O"):
            dir_index = index_of_dir(dir, directions)
            if(dir_index >= 3): 
                dir_index = 0
            else: 
                dir_index += 1
            # print(dir_index)
            dir = directions[list(directions.keys())[dir_index]]
            # print("Direction Change")        
            map[guard_pos[0]][guard_pos[1]] = "+"

        else:
            map[next_pos[0]][next_pos[1]] = "^"
            if map[guard_pos[0]][guard_pos[1]] != "+":
                if((dir[0]) == 1): dir_char = "d"                
                elif((dir[0]) == -1): dir_char = "u"
                elif((dir[1]) == 1): dir_char = "r"
                elif((dir[1]) == -1): dir_char = "l"

                map[guard_pos[0]][guard_pos[1]] = dir_char
            guard_pos = next_pos
    else:
        in_range = False
        if map[guard_pos[0]][guard_pos[1]] != "+":
            if((dir[0]) == 1): dir_char = "d"                
            elif((dir[0]) == -1): dir_char = "u"
            elif((dir[1]) == 1): dir_char = "r"
            elif((dir[1]) == -1): dir_char = "l"

            map[guard_pos[0]][guard_pos[1]] = dir_char
    return loop, in_range, map, guard_pos, dir

def calc_loop_path(map, guard_pos):
    path_map = map.copy()
    guard_in_range = True
    directions = {"up":(-1,0), "right":(0,1), "down":(1,0), "left":(0,-1)}
    dir = directions["up"]
    loop = False

    while(guard_in_range and loop == False):
        loop, guard_in_range, path_map, guard_pos, dir = move_guard_loop(path_map, guard_pos, dir)
    # print("=================")
    # print_map(path_map)
    return loop

def add_obstructions(map, guard_pos):
    new_map = copy.deepcopy(map)
    num_obstructions = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if(map[row][col] == "."):
                print(f"Check obstacle position {row},{col}")
                new_map[row][col] = "O"
                # print("==============")
                # print_map(new_map)
                if calc_loop_path(new_map, guard_pos) == True: num_obstructions += 1
                new_map = copy.deepcopy(map)
    return num_obstructions

map, guard_pos = parse_input()
map2, guard_pos = parse_input()

# path_map = calc_path(map, guard_pos)
# num_loops = add_obstructions(map2, guard_pos)


G = {i+j*1j: c for i,r in enumerate(open('input.txt'))
               for j,c in enumerate(r.strip())}

start = min(p for p in G if G[p] == '^')

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        if G.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print(len(path),
      sum(walk(G | {o: '#'})[1] for o in path))

# print(f"The guard covers {count_paths(path_map)} positions")
# print(f"There are {num_loops} obstacle positions that cause loops")  

