# First part

north = "north"
east = "east"
south = "south"
west = "west"

sides = {
    north: [-1, 0],
    east: [0, 1],
    south: [1, 0],
    west: [0, -1]
}

tiles = {
    # | is a vertical pipe connecting north and south.
    "|": [north, south],
    # - is a horizontal pipe connecting east and west.
    "-": [east, west],
    # L is a 90-degree bend connecting north and east.
    "L": [north, east],
    # J is a 90-degree bend connecting north and west.
    "J": [north, west],
    # 7 is a 90-degree bend connecting south and west.
    "7": [south, west],
    # F is a 90-degree bend connecting south and east.
    "F": [south, east],
    # . is ground; there is no pipe in this tile.
    ".": []
    # S is the starting position of the animal; there is a pipe on this
}

def coordsEqual(a, b):
    return "".join(set([str(a[x] - b[x]) for x in range(0, len(a))])) == "0"

def addCords(a, b):
    return [a[x] + b[x] for x in range(0, len(a))]

def getValueOnCoords(ground, coords):
    return ground[coords[0]][coords[1]]

def getValueOnSide(ground, coords, side):
    return getValueOnCoords(
        ground,
        addCords(coords, sides[side])
    )

def first():
    ground = []
    start = None

    with open("data.txt", "r") as file:
        i = 0
        for line in file:
            ground.append(list(line.strip()))
            for j in range(0, len(ground[-1])):
                if ground[i][j] == "S":
                    start = [i, j]
                    break
            i += 1

    startDirections = []
    if getValueOnSide(ground, start, north) in ["|", "7", "F"]:
        startDirections.append(north)
    else:
        startDirections.append(south)
    if getValueOnSide(ground, start, east) in ["-", "J", "7"]:
        startDirections.append(east)
    else:
        startDirections.append(west)

    paths = [[start, addCords(start, sides[x])] for x in startDirections]

    while True:
        for path in paths:
            nextSteps = tiles[getValueOnCoords(ground, path[-1])]
            for nextSide in nextSteps:
                nextStepCoords = addCords(path[-1], sides[nextSide])
                if not coordsEqual(path[-2], nextStepCoords):
                    path.append(nextStepCoords)
                    break

        if paths[0][-1] in paths[1] or paths[1][-1] in paths[0]:
            break

    result = max([len(path)-1 for path in paths])
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
