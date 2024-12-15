# First part

WALL = '#'
ROBOT = '@'
BOX = 'O'
SPACE = '.'
INSTRUCTION_TO_MOVEMENT = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1, 0],
    '<': [0, -1],
}

def printMap(size, robot, boxes, walls):
    print(WALL * (size[0] + 2))
    for i in range(size[0]):
        print(WALL, end='')
        for j in range(size[1]):
            if i == robot[0] and j == robot[1]:
                print(ROBOT, end='')
            elif [i, j] in boxes:
                print(BOX, end='')
            elif [i, j] in walls:
                print(WALL, end='')
            else:
                print(SPACE, end='')
        print(WALL)
    print(WALL * (size[0] + 2))

def isCoordsOnMap(size, coords):
    return coords[0] in range(size[0]) and coords[1] in range(size[1])

def addCoords(a, b):
    return [a[0]+b[0], a[1]+b[1]]

def getBoxesToMove(size, robot, boxes, walls, direction):
    boxesToMove = [addCoords(robot, direction)]
    while isCoordsOnMap(size, boxesToMove[-1]):
        nextPos = addCoords(boxesToMove[-1], direction)
        if nextPos in walls:
            return []
        elif nextPos in boxes:
            boxesToMove.append(nextPos)
            continue
        else:
            if isCoordsOnMap(size, addCoords(boxesToMove[-1], direction)):
                return boxesToMove
            else:
                return []
    return []

def first():
    warehouseSize = [0, 0]
    robotCoords = [0, 0]
    boxCoords = []
    wallCoords = []

    with open("data.txt", "r") as file:
        loadingMap = True
        for line in file:
            line = line.strip()

            if line == "":
                loadingMap = False

            elif loadingMap:
                line = line[1:-1]
                if line.strip(WALL) == "":
                    continue

                warehouseSize[0] += 1
                warehouseSize[1] = len(line)

                for j in range(warehouseSize[1]):
                    if line[j] == BOX:
                        boxCoords.append([warehouseSize[0] - 1, j])
                    elif line[j] == WALL:
                        wallCoords.append([warehouseSize[0] - 1, j])
                    elif line[j] == ROBOT:
                        robotCoords = [warehouseSize[0] - 1, j]

            else:
                for instruction in line:
                    movement = INSTRUCTION_TO_MOVEMENT[instruction]

                    newRobotCoords = addCoords(robotCoords, movement)

                    if isCoordsOnMap(warehouseSize, newRobotCoords):
                        if newRobotCoords in wallCoords:
                            pass
                        elif newRobotCoords in boxCoords:
                            boxesToMove = getBoxesToMove(warehouseSize, robotCoords, boxCoords, wallCoords, movement)
                            if len(boxesToMove):
                                for box in boxesToMove:
                                    boxCoords.remove(box)
                                for box in boxesToMove:
                                    boxCoords.append(addCoords(box, movement))
                                robotCoords = newRobotCoords
                        else:
                            robotCoords = newRobotCoords

    result = 0
    for box in boxCoords:
        result += (box[0]+1)*100 + box[1]+1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
