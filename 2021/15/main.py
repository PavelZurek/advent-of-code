# First part

def getData():
    data = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            data.append(list(map(int, list(line.strip()))))

    return data

neighbour_coords = [[-1, 0],[0, -1]]

def getDistanceMap(data):
    distances = [[0 for j in range(len(data[i]))] for i in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == j == 0:
                continue

            neighbour_values = []
            for nc in neighbour_coords:
                x = i + nc[0]
                y = j + nc[1]

                if 0 <= x < len(distances) and 0 <= y < len(distances[i]):
                    neighbour_values.append(distances[x][y])

            distances[i][j] = min(neighbour_values) + data[i][j]

    return distances

def first():
    data = getData()
    distances = getDistanceMap(data)

    result = distances.pop().pop()
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

second()
