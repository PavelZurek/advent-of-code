neighbour_coords = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def getData():
    data = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            data.append(line.strip())

    return data

def getLocalMinsCoords(data):
    local_mins = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            is_local_min = True
            for nc in neighbour_coords:
                x = i + nc[0]
                y = j + nc[1]

                if 0 <= x < len(data) and 0 <= y < len(data[i]):
                    if int(data[i][j]) >= int(data[x][y]):
                        is_local_min = False

            if is_local_min:
                local_mins.append([i, j])

    return local_mins


# First part

def first():
    data = getData()
    local_mins = getLocalMinsCoords(data)

    result = 0
    for local_min in local_mins:
        result += int(data[local_min[0]][local_min[1]]) + 1

    print("First: {}".format(result))

first()

# Second part

def second():
    data = getData()
    local_mins = getLocalMinsCoords(data)

    groups = [[local_mins[i]] for i in range(len(local_mins))]

    for i in range(len(groups)):
        change = True
        while(change):
            change = False
            for j in range(len(groups[i])):
                coords = groups[i][j]

                for nc in neighbour_coords:
                    x = coords[0] + nc[0]
                    y = coords[1] + nc[1]

                    if 0 <= x < len(data) and 0 <= y < len(data[x]):
                        if data[x][y] != '9':
                            if [x, y] not in groups[i]:
                                groups[i].append([x, y])
                                change = True

    groups.sort(key=len)

    result = 1
    for i in range(1, 4):
        result = result * len(groups[len(groups)-i])

    print("Second: {}".format(result))

second()
