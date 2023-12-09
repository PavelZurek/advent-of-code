# First part

def first():
    with open("data.txt", "r") as file:
        directions = next(file).strip()

        nodes = {}
        for line in file:
            if line == "\n":
                continue
            key, value = line.strip().split(" = ")
            L, R = value.strip("()").split(", ")
            nodes[key] = { "L": L, "R": R }

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
    result = 0
    print("Second: {}".format(result))

#second()
