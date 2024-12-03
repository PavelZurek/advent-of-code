import re

# First part

def first():
    with open("data.txt", "r") as file:
        line = file.read().strip()
        mul_instructions = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line)
        mul_instruction_params = [list(map(int, [re.sub('[^\d\.]', '', y) for y in x.split(',')])) for x in mul_instructions]
        result = sum([x[0]*x[1] for x in mul_instruction_params])
        print("First: {}".format(result))

first()

# Second part

def second():
    with open("data.txt", "r") as file:
        line = file.read().strip()
        instructions = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", line)

        result = 0
        add = True

        for instruction in instructions:
            if instruction == 'don\'t()':
                add = False
            elif instruction == 'do()':
                add = True
            else:
                if add:
                    mul_instruction_params = list(map(int, [re.sub('[^\d\.]', '', y) for y in instruction.split(',')]))
                    result += mul_instruction_params[0]*mul_instruction_params[1]

        print("Second: {}".format(result))

second()
