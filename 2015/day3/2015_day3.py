def calc_num_houses_santa():
    numHouses = 1
    x = 0
    y = 0
    address = f"{x},{y}"
    dictHouses = {address : 1}


    for line in open("input.txt"):
        for i in range(len(line)):
            if(line[i] == '^'): y += 1
            elif(line[i] == 'v'): y -= 1
            elif(line[i] == '>'): x += 1
            elif(line[i] == '<'): x -= 1
            address = f"{x},{y}"

            if is_new_house(dictHouses, address): 
                numHouses += 1
                dictHouses[address] = 1
            else:
                dictHouses[address] += 1

    return numHouses

def calc_num_houses_santa_robo():
    numHouses = 1
    sx = 0
    sy = 0
    rx = 0
    ry = 0
    address = f"{sx},{sy}"
    dictHouses = {address : 1}


    for line in open("input.txt"):
        for i in range(len(line)):
            if(i % 2 == 0):
                if(line[i] == '^'): sy += 1
                elif(line[i] == 'v'): sy -= 1
                elif(line[i] == '>'): sx += 1
                elif(line[i] == '<'): sx -= 1
                address = f"{sx},{sy}"
            else:
                if(line[i] == '^'): ry += 1
                elif(line[i] == 'v'): ry -= 1
                elif(line[i] == '>'): rx += 1
                elif(line[i] == '<'): rx -= 1
                address = f"{rx},{ry}"

            if is_new_house(dictHouses, address): 
                numHouses += 1
                dictHouses[address] = 1
            else:
                dictHouses[address] += 1

    return numHouses

def is_new_house(dict, address): 
    if address in dict.keys(): 
        return False
    return True
       


houses = calc_num_houses_santa()
print("The number of houses santa visits: ", houses)

houses = calc_num_houses_santa_robo()
print("The number of houses santa and robo visits: ", houses)


# bow = calc_bow()
# print("The bow needed is: ", bow)
