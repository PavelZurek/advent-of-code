neighbour_coords = [
    [-1, -1], [-1, 0], [-1, 1],
    [ 0, -1],          [ 0, 1],
    [ 1 ,-1], [ 1, 0], [ 1, 1]
]

def getData():
    data = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            data.append(list(map(int, line.strip())))

    return data

# First part

def first():
    data = getData()
    result = 0

    for _ in range(100):
        is_flashing = []
        flashed = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                if data[i][j] > 9:
                    is_flashing.append([i, j])

        while len(is_flashing) > 0:
            cur = is_flashing.pop(0)
            flashed.append(cur)
            data[cur[0]][cur[1]] = 0
            result += 1

            for nc in neighbour_coords:
                x = cur[0] + nc[0]
                y = cur[1] + nc[1]

                if 0 <= x < len(data) and 0 <= y < len(data[x]):
                    if data[x][y] != 0:
                        data[x][y] += 1

                        if data[x][y] > 9 and [x, y] not in is_flashing and [x, y] not in flashed:
                            is_flashing.append([x, y])

    print("First: {}".format(result))

first()

# Second part

def second():
    data = getData()
    
    total_count = len(data) * len(data[0])
    flash_count = 0
    result = 0

    while flash_count < total_count:
        result += 1
        flash_count = 0
        is_flashing = []
        flashed = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                if data[i][j] > 9:
                    is_flashing.append([i, j])

        while len(is_flashing) > 0:
            cur = is_flashing.pop(0)
            flashed.append(cur)
            data[cur[0]][cur[1]] = 0
            flash_count += 1

            for nc in neighbour_coords:
                x = cur[0] + nc[0]
                y = cur[1] + nc[1]

                if 0 <= x < len(data) and 0 <= y < len(data[x]):
                    if data[x][y] != 0:
                        data[x][y] += 1

                        if data[x][y] > 9 and [x, y] not in is_flashing and [x, y] not in flashed:
                            is_flashing.append([x, y])

    print("Second: {}".format(result))

second()
