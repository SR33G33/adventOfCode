def parse_input():
    test_vals = []
    equations = []

    with open("input.txt") as file:
        for line in file:
            line = line.split(":")
            test_vals.append(int(line[0].strip()))
            equation = line[1]
            cleaned_equation = []
            equation = (equation.split(" "))
            for number in equation:
                if(number != "" and number != "\n"):
                    cleaned_equation.append(int(number.strip()))
            equations.append(cleaned_equation)

    return test_vals, equations  # Count the number of lights that are on

def is_valid(target, equation):
    if len(equation) == 1:
        return equation[0]==target
    if is_valid(target, [equation[0]+equation[1]] + equation[2:]):
        return True
    if is_valid(target, [equation[0]*equation[1]] + equation[2:]):
        return True

    return False

def is_valid_cat(target, equation):
    if len(equation) == 1:
        return equation[0]==target
    if is_valid_cat(target, [equation[0]+equation[1]] + equation[2:]):
        return True
    if is_valid_cat(target, [equation[0]*equation[1]] + equation[2:]):
        return True
    if is_valid_cat(target, [int(str(equation[0])+str(equation[1]))] + equation[2:]):
        return True

    return False

def check_equations(vals, equations):
    sum = 0
    for equation_i in range(len(equations)):
        if(is_valid(vals[equation_i], equations[equation_i])): sum += vals[equation_i]
    return sum

def check_equations_cat(vals, equations):
    sum = 0
    for equation_i in range(len(equations)):
        # print(f"checking equn: {equation_i}: {equations[equation_i]}")
        if(is_valid_cat(vals[equation_i], equations[equation_i])): sum += vals[equation_i]
    return sum

test_vals, equations = parse_input()
sum = check_equations(test_vals, equations)

print(f"Total Sum of successful tests is {sum}")

sum = check_equations_cat(test_vals, equations)

print(f"Total Sum of successful tests with || is {sum}")

