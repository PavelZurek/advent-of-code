def getCounts():
    data = []

    with open("data.txt", "r") as file:
        data = list(map(int, file.readline().strip().split(',')))

    counts = [0 for _ in range(max(data) + 1)]
    for i in data:
        counts[i] += 1

    return counts

# First part

def getFuelRequirementPart1(depth, counts):
    fuel = 0

    for i in range(len(counts)):
        fuel += abs(counts[i] * (i - depth))

    return fuel

def first():
    counts = getCounts()

    minFuel = getFuelRequirementPart1(0, counts)
    for i in range(1, len(counts)):
        fuel = getFuelRequirementPart1(i, counts)
        if fuel < minFuel:
            minFuel = fuel

    result = minFuel
    print("First: {}".format(result))

first()

# Second part

def getFuelRequirementPart2(depth, counts):
    fuel = 0

    for i in range(len(counts)):
        if counts[i] > 0:
            dist = abs(i - depth)
            fuelCost = sum(range(0, dist + 1))
            fuel += fuelCost * counts[i]

    return fuel

def second():
    counts = getCounts()

    minFuel = getFuelRequirementPart2(0, counts)
    for i in range(1, len(counts)):
        fuel = getFuelRequirementPart2(i, counts)
        if fuel < minFuel:
            minFuel = fuel

    result = minFuel
    print("Second: {}".format(result))

second()
