# First part

def first():
    heightMap = []

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            heightMap.append(list(map(int, list(line))))

    result = 0

    for i in range(len(heightMap)):
        for j in range(len(heightMap[i])):
            height = heightMap[i][j]
            if height == 0:
                steps = [[[i,j]]]
                for x in range(9):
                    steps.append([])
                    for lastStep in steps[x]:
                        for neighbourCoords in [[0,1], [1,0], [0,-1], [-1,0]]:
                            nI = lastStep[0] + neighbourCoords[0]
                            nJ = lastStep[1] + neighbourCoords[1]
                            if nI in range(len(heightMap)) and nJ in range(len(heightMap[nI])) and heightMap[nI][nJ] == x+1:
                                if [nI, nJ] not in steps[x+1]:
                                    steps[x+1].append([nI, nJ])
                result += len(steps[-1])

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
