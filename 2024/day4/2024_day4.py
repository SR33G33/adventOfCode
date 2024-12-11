import math

def parse_input():
    word_search = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                word_search.append(line.strip())

    # print(word_search)
    return word_search  # Count the number of lights that are on


def search(grid, word, row, col, x, y):
    m = len(grid)
    n = len(grid[0])

    currX, currY = row + x, col + y
    k = 1

    while k < len(word):

        if currX >= m or currX < 0 or currY >= n or currY < 0:
            break

        if grid[currX][currY] != word[k]:
            break

        currX += x
        currY += y
        k += 1

    if k == len(word):
        return True

    return False

def find_word(word_search, word):
    count = 0

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for row in range(len(word_search[0])):
        for col in range(len(word_search)):
            if(word_search[row][col] == word[0]):
                for i in range(8):
                    if(search(word_search, word, row, col, x[i], y[i])): count += 1
    return count

def find_word(word_search, word):
    count = 0

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for row in range(len(word_search[0])):
        for col in range(len(word_search)):
            if(word_search[row][col] == word[0]):
                for i in range(8):
                    if(search(word_search, word, row, col, x[i], y[i])): count += 1
    return count

def find_word_cross(data):
    rows, cols = len(data), len(data[0])
    count = 0

    _set = {"M", "S"}

    # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                    count += 1

    return count

word_search = parse_input()
search_word = "XMAS"
search_word2 = "MAS"

print(f"The word {search_word} is found {find_word(word_search, search_word)}")
print(f"The word {search_word2} is found {find_word_cross(word_search)}")

