# First part

def first():
    data = []
    neighbour_coords = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            data.append(line.strip())

    result = 0

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
                result += int(data[i][j]) + 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
