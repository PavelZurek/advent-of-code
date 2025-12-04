# First part

def getRollsCount(rolls_map, i, j):
    count = 0
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k >= 0 and l >= 0 and k < len(rolls_map) and l < len(rolls_map[k]) and rolls_map[k][l] == "@":
                count += 1
    return count

def first():
    result = 0
    rolls_map = []

    with open("data.txt", "r") as file:
        for line in file:
            rolls_map.append(line.strip())

    for i in range(len(rolls_map)):
        for j in range(len(rolls_map[i])):
            if rolls_map[i][j] == "@":
                if getRollsCount(rolls_map, i, j) < 5:
                    result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
