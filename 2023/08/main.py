from math import lcm

def load():
    with open("data.txt", "r") as file:
        directions = next(file).strip()

        nodes = {}
        for line in file:
            if line == "\n":
                continue
            key, value = line.strip().split(" = ")
            L, R = value.strip("()").split(", ")
            nodes[key] = { "L": L, "R": R }

        return [nodes, directions]

# First part

def first():
    nodes, directions = load()

    step = 0
    current = "AAA"
    target = "ZZZ"
    while not current == target:
        direction = directions[step % len(directions)]
        step += 1
        current = nodes[current][direction]

    result = step
    print("First: {}".format(result))

first()

# Second part

def second():
    nodes, directions = load()

    pointers = []
    for node in nodes:
        if node[-1] == "A":
            pointers.append(node)

    steps = [0 for _ in range(0, len(pointers))]
    for i in range(0, len(pointers)):
        while not pointers[i][-1] == "Z":
            direction = directions[steps[i] % len(directions)]
            steps[i] += 1
            pointers[i] = nodes[pointers[i]][direction]

    result = lcm(*steps)
    print("Second: {}".format(result))

second()
