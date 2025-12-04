def loadMap():
    rolls_map = []

    with open("data.txt", "r") as file:
        for line in file:
            rolls_map.append(list(line.strip()))

    return rolls_map

def getRollsCount(rolls_map, i, j):
    count = 0
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k >= 0 and l >= 0 and k < len(rolls_map) and l < len(rolls_map[k]) and rolls_map[k][l] == "@":
                count += 1
    return count

# First part

def first():
    result = 0
    rolls_map = loadMap()

    for i in range(len(rolls_map)):
        for j in range(len(rolls_map[i])):
            if rolls_map[i][j] == '@':
                if getRollsCount(rolls_map, i, j) < 5:
                    result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    change = True
    rolls_map = loadMap()

    while change:
        change = False
        for i in range(len(rolls_map)):
            for j in range(len(rolls_map[i])):
                if rolls_map[i][j] == "@":
                    if getRollsCount(rolls_map, i, j) < 5:
                        result += 1
                        rolls_map[i][j] = '.'
                        change = True

    print("Second: {}".format(result))

second()
