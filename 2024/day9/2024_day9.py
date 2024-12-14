def parse_input():
    map = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                for char in line:
                    if(char != "\n" and char != ""):
                        map.append(char)
    # print(map)
    return map  

def generate_disk_image(disk_map):
    full_list = []
    empty_list = []
    id_locations = []

    disk_image = []
    is_space = False
    id = 0
    for index in range(len(disk_map)):
        if(not is_space):
            full_list.append((len(disk_image), int(disk_map[index]) , id))
            for i in range(int(disk_map[index])):
                disk_image.append(id)
            id += 1
            is_space = True
        else:
            empty_list.append((len(disk_image), int(disk_map[index])))
            for i in range(int(disk_map[index])):
                disk_image.append(".")
            is_space = False

    return disk_image, full_list, empty_list

def get_last_num(disk_image):
    for i in range(len(disk_image)-1, -1, -1):
        if(disk_image[i] != "."): return i
    return -1

def reassemble_string(string_list):
    string = ""
    for i in range(len(string_list)):
        string += string_list[i]
    return string

def swap(a, b, string):
    # print(string)
    # string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    # string = reassemble_string(string)
    return string

def compress_disk_map(disk_map):
    disk_image, full_blocks, empty_blocks = generate_disk_image(disk_map)
    # print(disk_image)
    # print(full_blocks)
    # print(empty_blocks)

    for i in range(len(disk_image)):
        # print(f"Checking {i}/{len(disk_image)}")
        if(disk_image[i] == "."):
            swap_index = get_last_num(disk_image)
            if(i < swap_index): 
                # print(f"Swapping {disk_image[i]} and {disk_image[swap_index]}")
                disk_image = swap(i, swap_index, disk_image)
            else: break
            # print(disk_image)
    return disk_image

def compress_disk_map_p2(disk_map):
    disk_image, full_blocks, empty_blocks = generate_disk_image(disk_map)
    empty_block_pointer = 0

    for block_pointer in range(len(full_blocks)-1, -1, -1):
        # print(f"Checking {len(full_blocks)-block_pointer}/{len(full_blocks)}")

        for empty_block_pointer in range(len(empty_blocks)):

            curr_block = full_blocks[block_pointer]
            curr_empty_block = empty_blocks[empty_block_pointer]

            empty_space = curr_empty_block[1]
            empty_loc = curr_empty_block[0]

            loc = curr_block[0]
            size = curr_block[1]
            id = curr_block[2]

            if(size <= empty_space):
                for j in range(size):
                    swap(empty_loc + j, loc + j, disk_image)
                # print(disk_image)
                empty_blocks[empty_block_pointer] = (empty_loc+size, empty_space-size)
                # print(empty_blocks)
                break
    return disk_image


def calc_checksum(disk_image):
    sum = 0
    for i in range(len(disk_image)):
        if(disk_image[i] != "."):
            sum += int(disk_image[i])*i
    return sum

disk_map = parse_input()
# compressed_disk = compress_disk_map(disk_map)
compressed_disk_p2 = compress_disk_map_p2(disk_map)


# print(f"There are {calc_checksum(compressed_disk)} antinodes")
print(f"There are {calc_checksum(compressed_disk_p2)} antinodes for p2")


