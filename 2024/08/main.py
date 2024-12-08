# First part

def printMap(size, antenasByFrequence, antinodes):
    print('Size:', size)
    print('Antenas:', antenasByFrequence)
    print('Antinodes:', antinodes)

    map = [['.' for _ in range(size[1])] for _ in range(size[0])]
    for antinode in antinodes:
        map[antinode[0]][antinode[1]] = '#'
    for frequence, antenas in antenasByFrequence.items():
        for antena in antenas:
            map[antena[0]][antena[1]] = frequence

    for i in range(size[0]):
        for j in range(size[1]):
            print(map[i][j], end='')
        print()

def first():
    mapSize = [0, 0]
    antenasByFrequence = {}

    i = 0
    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            mapSize[0] +=1
            mapSize[1] = len(line)
            for j in range(len(line)):
                if line[j] != '.':
                    if line[j] not in antenasByFrequence:
                        antenasByFrequence[line[j]] = []
                    antenasByFrequence[line[j]].append([i, j])
            i+=1

    antinodes = []
    for _, antenas in antenasByFrequence.items():
        for i in range(len(antenas)):
            for j in range(i, len(antenas)):
                if i != j:
                    distance = [antenas[i][0] - antenas[j][0], antenas[i][1] - antenas[j][1]]
                    newAntinodes = [
                        [antenas[i][0] + distance[0], antenas[i][1] + distance[1]],
                        [antenas[j][0] - distance[0], antenas[j][1] - distance[1]]
                    ]
                    for antinode in newAntinodes:
                        if antinode[0] in range(0, mapSize[0]) and antinode[1] in range(0, mapSize[0]) and antinode not in antinodes:
                            antinodes.append(antinode)

    #printMap(mapSize, antenasByFrequence, antinodes)

    result = len(antinodes)
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
