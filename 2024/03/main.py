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
    result = 0
    print("Second: {}".format(result))

#second()
