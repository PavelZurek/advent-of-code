from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def turn(dir):
    if dir == Direction.UP:
        return Direction.RIGHT
    elif dir == Direction.RIGHT:
        return Direction.DOWN
    elif dir == Direction.DOWN:
        return Direction.LEFT
    elif dir == Direction.LEFT:
        return Direction.UP

def getMovement(dir):
    if dir == Direction.UP:
        return [-1, 0]
    elif dir == Direction.DOWN:
        return [1, 0]
    if dir == Direction.LEFT:
        return [0, -1]
    elif dir == Direction.RIGHT:
        return [0, 1]

# First part

class Guard():
    def __init__(self, map):
        self.map = map
        self.dir = Direction.UP
        self.pos = [0, 0]
        for i in range(0, len(map)):
            for j in range(0, len(map[i])):
                if map[i][j] == '^':
                    self.pos = [i, j]

    def isPosOnMap(self, pos):
        return pos[0] in range(0, len(self.map)) and pos[1] in range(0, len(self.map[0]))

    def isOnMap(self):
        return self.isPosOnMap(self.pos)

    def getNextPos(self):
        movement = getMovement(self.dir)
        return [self.pos[0]+movement[0], self.pos[1]+movement[1]]

    def canMove(self):
        newPos = self.getNextPos()
        return not self.isPosOnMap(newPos) or self.map[newPos[0]][newPos[1]] != '#'
    
    def turn(self):
        self.dir = turn(self.dir)

    def move(self):
        while not self.canMove():
            self.turn()
        self.map[self.pos[0]][self.pos[1]] = 'X'
        self.pos = self.getNextPos()
        if (not self.isOnMap()):
            return False
        self.map[self.pos[0]][self.pos[1]] = '^'
        return True

    def printMap(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                print(self.map[i][j], end='')
            print()

def first():
    map = []
    with open("data.txt", "r") as file:
        for line in file:
            map.append(list(line.strip()))

    guard = Guard(map)

    while guard.isOnMap():
        if not guard.move():
            break

    result = 0

    for i in range(0, len(guard.map)):
        for j in range(0, len(guard.map[i])):
            if guard.map[i][j] == 'X':
                result += 1

    print("First: {}".format(result))

first()

# Second part

def addPositions(posA, posB):
    return [posA[0] + posB[0], posA[1] + posB[1]]

class SecondGuard():
    def __init__(self):
        self.visitedEdgeHashes = []
        self.outOfMap = False
        self.inLoop = False
        self.dir = Direction.UP

        self.map = []
        with open("data.txt", "r") as file:
            for line in file:
                self.map.append(list(line.strip()))

        self.pos = [0, 0]
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] == '^':
                    self.pos = [i, j]
                    self.map[i][j] = 'X'

    def getPosHash(self):
        return '{}{}'.format(self.pos, self.dir)

    def getNextPos(self):
        oldPos = self.pos
        movement = getMovement(self.dir)

        newPos = oldPos
        while newPos[0] in range(0, len(self.map)) and newPos[1] in range(0, len(self.map[0])) and self.map[newPos[0]][newPos[1]] != '#':
            oldPos = newPos
            newPos = addPositions(newPos, movement)

        return oldPos

    def move(self):
        if self.outOfMap or self.inLoop:
            return

        oldPos = self.pos
        self.pos = self.getNextPos()
        if oldPos[0] == self.pos[0]:
            start = min(oldPos[1], self.pos[1])
            end = max(oldPos[1], self.pos[1])
            for i in range(start, end+1):
                self.map[oldPos[0]][i] = 'X'
        if oldPos[1] == self.pos[1]:
            start = min(oldPos[0], self.pos[0])
            end = max(oldPos[0], self.pos[0])
            for i in range(start, end+1):
                self.map[i][oldPos[1]] = 'X'

        newPos = addPositions(getMovement(self.dir), self.pos)
        if newPos[0] not in range(0, len(self.map)) or newPos[1] not in range(0, len(self.map[0])):
            self.outOfMap = True

    def turn(self):
        if self.outOfMap or self.inLoop:
            return

        while True:
            self.dir = turn(self.dir)
            movement = getMovement(self.dir)
            facingPos = addPositions(self.pos, movement)
            if self.map[facingPos[0]][facingPos[1]] != '#':
                break

        if self.getPosHash() in self.visitedEdgeHashes:
            self.inLoop = True
        else:
            self.visitedEdgeHashes.append(self.getPosHash())

    def isInLoop(self):
        while not self.outOfMap and not self.inLoop:
            self.move()
            self.turn()

        return self.inLoop

    def print(self):
        print('Guard at {} facing {}'.format(self.pos, self.dir), end='')
        if self.outOfMap:
            print(' - OUT OF MAP', end='')
        if self.inLoop:
            print(' - IN LOOP', end='')
        print()
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if i == self.pos[0] and j == self.pos[1]:
                    print('^', end='')
                else:
                    print(self.map[i][j], end='')
            print()

def second():
    original = SecondGuard()
    result = 0
    
    for i in range(0, len(original.map)):
        for j in range(0, len(original.map[i])):
            guard = SecondGuard()
            if i == guard.pos[0] and j == guard.pos[1]:
                continue
            guard.map[i][j] = '#'
            if (guard.isInLoop()):
                result += 1

    print("Second: {}".format(result))

second()
