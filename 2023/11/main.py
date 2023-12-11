# First part

def first():
    galaxies = []
    maxCoords = [0, 0]

    with open("data.txt", "r") as file:
        i = 0
        for line in file:
            j = 0
            for c in line:
                if c == "#":
                    galaxies.append([i, j])
                    if i > maxCoords[0]:
                        maxCoords[0] = i
                    if j > maxCoords[1]:
                        maxCoords[1] = j
                j += 1
            i += 1

    iSpaces, jSpaces = [[x for x in range(0, maxCoords[0]+1)], [x for x in range(0, maxCoords[1]+1)]]

    for g in galaxies:
        i, j = g
        if i in iSpaces: iSpaces.remove(i)
        if j in jSpaces: jSpaces.remove(j)

    maxCoords = [
        maxCoords[0] + len(iSpaces) + 1,
        maxCoords[1] + len(jSpaces) + 1
    ]

    for g in galaxies:
        for iSpace in reversed(iSpaces):
            if g[0] > iSpace:
                g[0] += 1
        for jSpace in reversed(jSpaces):
            if g[1] > jSpace:
                g[1] += 1

    distances = []
    for g1i in range(0, len(galaxies)):
        for g2i in range(g1i + 1, len(galaxies)):
            g1 = galaxies[g1i]
            g2 = galaxies[g2i]
            distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            distances.append(distance)

    result = sum(distances)
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
