mapSize = [101, 103]

class Robot():
    def __init__(self, line):
        posStr, velStr = line.strip().split(' ')
        self.pos = list(map(int, posStr.split('=')[1].split(',')))
        self.vel = list(map(int, velStr.split('=')[1].split(',')))

    def move(self, mapSize):
        self.pos = [
            (self.pos[0] + self.vel[0]) % mapSize[0],
            (self.pos[1] + self.vel[1]) % mapSize[1]
        ]

def loadRobots():
    robots = []

    with open("data.txt", "r") as file:
        for line in file:
            robots.append(Robot(line))

    return robots

def strigifyPos(pos):
    return ','.join(map(str, pos))

def posFromString(pos):
    return list(map(int, pos.split(',')))

def printMap(robots):
    robotCounts = getRobotCounts(robots)

    for i in range(mapSize[1]):
        for j in range(mapSize[0]):
            key = strigifyPos([j, i])
            if key in robotCounts:
                print(robotCounts[key] , end='')
            else:
                print('.', end='')
        print()

# First part

def getRobotCounts(robots):
    robotCounts = {}

    for robot in robots:
        key = strigifyPos(robot.pos)
        if key not in robotCounts:
            robotCounts[key] = 0
        robotCounts[key] += 1

    return robotCounts

def first():
    robots = loadRobots()

    for _ in range(100):
        for robot in robots:
            robot.move(mapSize)

    quadrantCounts = [0, 0, 0, 0]
    quadrantDividers = [int(x/2) for x in mapSize]
    robotCounts = getRobotCounts(robots)

    for key, count in robotCounts.items():
        pos = posFromString(key)

        if pos[0] < quadrantDividers[0]:
            if pos[1] < quadrantDividers[1]:
                quadrantCounts[0] += count
            elif pos[1] > quadrantDividers[1]:
                quadrantCounts[2] += count
        elif pos[0] > quadrantDividers[0]:
            if pos[1] < quadrantDividers[1]:
                quadrantCounts[1] += count
            elif pos[1] > quadrantDividers[1]:
                quadrantCounts[3] += count

    result = 1
    for c in quadrantCounts:
        result *= c

    print("First: {}".format(result))

first()

# Second part

def detectLine(robots, length):
    robotCounts = getRobotCounts(robots)
    line = False

    for i in range(mapSize[1]):
        lineLen = 0
        for j in range(mapSize[0]):
            key = strigifyPos([j, i])
            if key in robotCounts:
                lineLen += 1
                if lineLen >= length:
                    line = True
            else:
                lineLen = 0

    return line

def second():
    robots = loadRobots()
    result = 0

    lineDetected = False
    while not lineDetected:
        result += 1
        for robot in robots:
            robot.move(mapSize)
        lineDetected = detectLine(robots, 10)

    #printMap(robots)
    print("Second: {}".format(result))

second()
