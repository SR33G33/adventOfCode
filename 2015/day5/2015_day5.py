import hashlib

def num_good_strings():
    good_count = 0
    for line in open("input.txt"):
        if check_string(line): good_count += 1
    return good_count

def check_string(input):
    # return (check_vowels(input) and check_repeat(input) and check_banned(input))
    return check_new_cond(input)

def check_vowels(input):
    vowels = "aeiou"
    count = sum(input.count(vowel) for vowel in vowels)
    return (count > 2)

def check_repeat(input):
    for i in range(len(input)):
        if(i != 0):
            if(input[i] == input [i-1]): return True

def check_banned(input):
    banned = {"ab", "cd", "pq", "xy"}
    count = sum(input.count(ban) for ban in banned)
    return (count == 0)

def check_new_cond(input):
    check1 = False
    check2 = False
    for i in range(len(input) - 1):
        pair = input[i:i+2]
        if input.count(pair) > 1:
            check1 = True
            break
    for i in range(len(input) - 2):
        if input[i] == input[i + 2]:
            check2 = True
            break
    return (check1 and check2)


print("Num Good Strings: ", num_good_strings())

