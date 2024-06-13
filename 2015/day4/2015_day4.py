import hashlib

def find_hash_with_zeros():
    input = ''
    test_int = 0
    result = ''
    hashNum = 0

    for line in open("input.txt"):
        input = line
    
    while(check_hash(result) == False):
        hashNum = input + str(test_int)
        result = hashlib.md5(hashNum.encode()).hexdigest()
        # print(f'Trying: {test_int}')
        test_int += 1
    return (test_int - 1)

def check_hash(hash):
    if(hash[0:6] == "000000"):
        return True
    return False

print("Integer: ", find_hash_with_zeros())