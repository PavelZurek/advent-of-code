def getInstructions():
    instructions = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break

            splited = line.split(' ')
            instructions.append(
                {
                    'name': splited[0],
                    'argument': int(splited[1])
                }
            )

    return instructions

# First part

def first():
    instructions = getInstructions()

    visited = []
    accumulator = 0
    i = 0

    while True:
        if i in visited:
            break
        visited.append(i)

        ins = instructions[i]

        if ins.get('name') == 'nop':
            i = i + 1
        if ins.get('name') == 'acc':
            accumulator = accumulator + ins.get('argument')
            i = i + 1
        if ins.get('name') == 'jmp':
            i = i + ins.get('argument')

    result = accumulator
    print("First: {}".format(result))

first()

# Second part

def getAcumulatorValue(instructions):
    visited = []
    accumulator = 0
    i = 0

    while True:
        if i in visited:
            return [accumulator, False]
        if i >= len(instructions):
            return [accumulator, True]
        visited.append(i)

        ins = instructions[i]

        if ins.get('name') == 'nop':
            i = i + 1
        if ins.get('name') == 'acc':
            accumulator = accumulator + ins.get('argument')
            i = i + 1
        if ins.get('name') == 'jmp':
            i = i + ins.get('argument')

def second():
    instructions = getInstructions()

    for i in range(0, len(instructions)):
        if instructions[i].get('name') == 'acc':
            continue

        instructions2 = getInstructions()

        if instructions[i].get('name') == 'jmp':
            instructions2[i]["name"] = 'nop'
        if instructions[i].get('name') == 'nop':
            instructions2[i]["name"] = 'jmp'

        result, success = getAcumulatorValue(instructions2)
        if success:
            break

    print("Second: {}".format(result))

second()
