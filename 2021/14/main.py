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

# First part

def polymerization_step_part1(polymer, instructions):
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
        polymer = polymerization_step_part1(polymer, instructions)

    counts = getCounts(polymer)

    result = max(counts.values()) - min(counts.values())
    print("First: {}".format(result))

first()

# Second part

def polymerization_step_part2(pair_counts, instructions):
    result = {}

    for pair in pair_counts.keys():
        if pair not in instructions.keys():
            result[pair] = pair
        else:
            new_pair_counts = [pair[0] + instructions[pair], instructions[pair] + pair[1]]

            for new_pair in new_pair_counts:
                if new_pair in result.keys():
                    result[new_pair] += pair_counts[pair]
                else:
                    result[new_pair] = pair_counts[pair]

    return result

def second():
    polymer, instructions = getData()
    pair_counts = {}

    for i in range(len(polymer) - 1):
        key = ''.join(polymer[i:i + 2])

        if key not in pair_counts.keys():
            pair_counts[key] = 1
        else:
            pair_counts[key] += 1

    for _ in range(40):
        pair_counts = polymerization_step_part2(pair_counts, instructions)

    total_counts = {}
    for pair in pair_counts.keys():
        char = pair[0]

        if char in total_counts.keys():
            total_counts[char] += pair_counts[pair]
        else:
            total_counts[char] = pair_counts[pair]

    total_counts[polymer.pop()] += 1

    result = max(total_counts.values()) - min(total_counts.values())
    print("Second: {}".format(result))

second()
