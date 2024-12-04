def loadData():
    data = []

    with open("data.txt", "r") as file:
        for line in file:
            data.append(line.strip())

    return data

# First part

from enum import Enum
class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    DOWN_RIGHT = 4
    DOWN_LEFT = 5
    UP_RIGHT = 6
    UP_LEFT = 7

word = 'XMAS'

def first():
    data = loadData()
    result = 0

    for i in range(0, len(data)):
        line = data[i]
        for j in range(0, len(line)):
            matches = {}
            for d in Direction:
                matches[d] = 0

            for x in range(0, len(word)):
                if j+x < len(data[i]) and data[i][j+x] == word[x]:
                    matches[Direction.RIGHT] += 1
                if j-x >= 0 and data[i][j-x] == word[x]:
                    matches[Direction.LEFT] += 1

                if i+x < len(data) and data[i+x][j] == word[x]:
                    matches[Direction.DOWN] += 1
                if i-x >=0 and data[i-x][j] == word[x]:
                    matches[Direction.UP] += 1

                if j+x < len(data[i]) and i+x < len(data) and data[i+x][j+x] == word[x]:
                    matches[Direction.DOWN_RIGHT] += 1
                if j-x >=0 and i+x < len(data) and data[i+x][j-x] == word[x]:
                    matches[Direction.DOWN_LEFT] += 1
                    
                if j+x < len(data[i]) and i-x >=0 and data[i-x][j+x] == word[x]:
                    matches[Direction.UP_RIGHT] += 1
                if j-x >= 0 and i-x >=0 and data[i-x][j-x] == word[x]:
                    matches[Direction.UP_LEFT] += 1

            for _, match in matches.items():
                if match == len(word):
                    result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    data = loadData()
    result = 0

    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            if data[i][j] == 'A':
                if data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S' and data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S':
                    result += 1
                if data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S' and data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M':
                    result += 1
                if data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M' and data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S':
                    result += 1
                if data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M' and data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M':
                    result += 1

    print("Second: {}".format(result))

second()
