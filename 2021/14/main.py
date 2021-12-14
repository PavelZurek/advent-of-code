# First part

def getData():

    polymer = []
    instructions = {}

    with open("data.txt", "r") as file:
        polymer = list(file.readline().strip())
        file.readline()

        i = file.readline().strip()
        while i != "":
            key, value = i.split(" -> ")
            instructions[key] = value

            i = file.readline().strip()

    return [polymer, instructions]

def getCounts(polymer):
    counts = {}

    for c in polymer:
        if c not in counts.keys():
            counts[c] = 0

        counts[c] += 1

    return counts

def polymerization_step(polymer, instructions):
    new_polymer = []

    for i in range(len(polymer) - 1):
        new_polymer.append(polymer[i])

        key = polymer[i] + polymer[i + 1]
        if key in instructions.keys():
            new_polymer.append(instructions[key])

    new_polymer.append(polymer.pop())

    return new_polymer

def first():
    polymer, instructions = getData()

    for _ in range(10):
        polymer = polymerization_step(polymer, instructions)

    counts = getCounts(polymer)

    print(counts)
    result = max(counts.values()) - min(counts.values())
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
