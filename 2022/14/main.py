EMPTY = '.'
ROCK = '#'
SAND = 'O'

def loadCaveMap(bottom=False):
    caveMap = [[EMPTY for j in range(0, 1000)] for i in range(0, 1000)]
    caveMap[500][0] = '+'
    maxY = 0

    with open("data.txt", "r") as file:
        for line in file:
            routePoints = line.strip(" \n").split(" -> ")
            for i in range(0, len(routePoints)):
                routePoints[i] = list(map(int, routePoints[i].split(',')))

            while (len(routePoints) > 1):
                currentPoint = routePoints.pop(0)
                nextPoint = routePoints[0]

                caveMap[currentPoint[0]][currentPoint[1]] = ROCK
                caveMap[nextPoint[0]][nextPoint[1]] = ROCK

                if currentPoint[0] != nextPoint[0]:
                    stepX = 1 if currentPoint[0] < nextPoint[0] else -1
                    for i in range(currentPoint[0], nextPoint[0]+stepX, stepX):
                        caveMap[i][currentPoint[1]] = ROCK

                if currentPoint[1] != nextPoint[1]:
                    stepY = 1 if currentPoint[1] < nextPoint[1] else -1
                    for j in range(currentPoint[1], nextPoint[1]+stepY, stepY):
                        caveMap[currentPoint[0]][j] = ROCK
                        if j > maxY:
                            maxY = j

    if bottom:
        for i in range(0, 1000):
            caveMap[i][maxY+2] = ROCK

    return caveMap

def getTargetCoords(caveMap, currentPoint):
    possibleMoves = [[0, 1], [-1, 1], [1, 1]]

    for move in possibleMoves:
        targetCoords = [currentPoint[0]+move[0], currentPoint[1]+move[1]]
        if caveMap[targetCoords[0]][targetCoords[1]] == EMPTY:
            return targetCoords

def getResult(caveMap):
    result = 0

    for i in range(0, 1000):
        for j in range(0, 1000):
            if caveMap[i][j] == SAND:
                result += 1

    return result

def printCave(caveMap):
    print("---------------------")
    for j in range(0, 12):
        for i in range(494, 504):
            print(caveMap[i][j], end='')
        print()
    print("---------------------")

# First part

def first():
    caveMap = loadCaveMap()

    while True:
        try:
            sandCoords = [500, 0]

            nextCoords = getTargetCoords(caveMap, sandCoords)
            while nextCoords != None:
                sandCoords = nextCoords
                nextCoords = getTargetCoords(caveMap, nextCoords)

            caveMap[sandCoords[0]][sandCoords[1]] = SAND
        except IndexError:
            break

    result = getResult(caveMap)
    print("First: {}".format(result))

first()

# Second part

def second():
    caveMap = loadCaveMap(True)

    while caveMap[500][0] != SAND:
        sandCoords = [500, 0]

        nextCoords = getTargetCoords(caveMap, sandCoords)
        while nextCoords != None:
            sandCoords = nextCoords
            nextCoords = getTargetCoords(caveMap, nextCoords)

        caveMap[sandCoords[0]][sandCoords[1]] = SAND

    result = getResult(caveMap)
    print("Second: {}".format(result))

second()
