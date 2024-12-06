# First part

from enum import Enum
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

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
        if self.dir == Direction.UP:
            return [self.pos[0]-1, self.pos[1]]
        elif self.dir == Direction.DOWN:
            return [self.pos[0]+1, self.pos[1]]
        if self.dir == Direction.LEFT:
            return [self.pos[0], self.pos[1]-1]
        elif self.dir == Direction.RIGHT:
            return [self.pos[0], self.pos[1]+1]
        
    def canMove(self):
        newPos = self.getNextPos()
        return not self.isPosOnMap(newPos) or self.map[newPos[0]][newPos[1]] != '#'
    
    def turn(self):
        if self.dir == Direction.UP:
            self.dir = Direction.RIGHT
        elif self.dir == Direction.RIGHT:
            self.dir = Direction.DOWN
        elif self.dir == Direction.DOWN:
            self.dir = Direction.LEFT
        elif self.dir == Direction.LEFT:
            self.dir = Direction.UP

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

def second():
    result = 0
    print("Second: {}".format(result))

#second()
