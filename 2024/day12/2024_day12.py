from collections import defaultdict

def parse_input():
    map = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                line_list = []
                for char in line:
                    if(char != "\n" and char != ""):
                        line_list.append((char))

                map.append(line_list)
    # print("============")
    return map  

def print_map(map):
    for row in map:
        if(row):
            row_string = ""
            for col in row:
                row_string += str(col) + "\t"
        print(row_string)

def calculate_fences(region_list, fence_list):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    fences = 0
    for region in region_list.keys():
        fences = 0
        plots = region_list[region]
        for plot in plots:
            fences += 4
            for direction in directions:
                if((plot[0] + direction[0], plot[1] + direction[1]) in plots): fences -= 1
        fence_list[region] = fences
    return fence_list

def calculate_cost(region_list, fence_list):
    price = 0
    for region in region_list.keys():
        price += len(region_list[region])*fence_list[region]
    return price

def dfs(map, empty_map, row, col, region_num):
    empty_map[row][col] = region_num
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    region = map[row][col]
    for direction in directions:
        newRow = row + direction[0]
        newCol = col + direction[1]
        if(newRow >= 0 and newRow < len(map) and newCol >=0 and newCol < len(map[0])):
            if(map[newRow][newCol] == region and empty_map[newRow][newCol] == 0): empty_map = dfs(map, empty_map, newRow, newCol, region_num)
    return empty_map

def flood_fill(farm):
    region_num = 1
    empty_farm = [[0 for col in range(len(farm))] for row in range(len(farm[0]))]
    for row in range(len(farm)):
        for col in range(len(farm[row])):
            if(empty_farm[row][col] == 0):
                empty_farm = dfs(farm, empty_farm, row, col, region_num)
                region_num += 1
    # print_map(empty_farm)
    return empty_farm

def grid_val(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return ' '

def calculate_corners(region_list, corner_list, map):
    directions = [(1,1), (-1,1), (1,-1), (-1,-1)]
    corners = 0
    for region in region_list.keys():
        corners = 0
        plots = region_list[region]
        for plot in plots:
            y = plot[0]
            x = plot[1]
            plot_val = map[y][x]


            plot_up = grid_val(map, y-1, x)
            plot_down = grid_val(map, y+1, x)
            plot_left = grid_val(map, y, x-1)
            plot_right = grid_val(map, y, x+1)

            # corners
            if plot_up != plot_val and plot_right != plot_val:
                corners += 1
            if plot_right != plot_val and plot_down != plot_val:
                corners += 1
            if plot_down != plot_val and plot_left != plot_val:
                corners += 1
            if plot_left != plot_val and plot_up != plot_val:
                corners += 1
            
            # 'negative' corners
            if grid_val(map, y-1, x-1) != plot_val and plot_up == plot_val and plot_left == plot_val:
                corners += 1
            if grid_val(map, y-1, x+1) != plot_val and plot_up == plot_val and plot_right == plot_val:
                corners += 1
            if grid_val(map, y+1, x+1) != plot_val and plot_down == plot_val and plot_right == plot_val:
                corners += 1
            if grid_val(map, y+1, x-1) != plot_val and plot_down == plot_val and plot_left == plot_val:
                corners += 1

        corner_list[region] = corners
    return corner_list

def find_regions(farm):
    region_list = {}
    fence_list = {}
    corner_list = {}
    for row in range(len(farm)):
        for col in range(len(farm[row])):
            region = farm[row][col]
            if region not in region_list:
                region_list[region] = []
                fence_list[region] = 0
                region_list[region].append((row, col))  
            else:
                region_list[region].append((row, col))
    
    fence_list = calculate_fences(region_list, fence_list)
    corner_list = calculate_corners(region_list, corner_list, farm)


    # print(region_list)
    # print(fence_list)
    print(corner_list)                 

    return calculate_cost(region_list, fence_list), calculate_cost(region_list, corner_list)

farm = parse_input()
farm = flood_fill(farm)
cost, side_cost = find_regions(farm)

print(f"The cost is {cost}")
print(f"The side cost is {side_cost}")

