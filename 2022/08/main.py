def getTreeMap():
    treeMap = []

    with open("data.txt", "r") as file:
        for line in file:
            treeMap.append(list(line.strip(" \n")))

    return treeMap

# First part

def first():
    treeMap = getTreeMap()
    result = 0

    for x in range(0, len(treeMap)):
        for y in range(0, len(treeMap[x])):
            # Edges are always visible
            if x==0 or x==(len(treeMap)-1) or y==0 or y==(len(treeMap[x])-1):
                result += 1
                continue

            treeHeight = treeMap[x][y]

            # Check
            visibleX1 = True
            for i in range(0, x):
                if treeMap[i][y] >= treeHeight:
                    visibleX1 = False
                    break

            visibleX2 = True
            for i in range(x+1, len(treeMap)):
                if treeMap[i][y] >= treeHeight:
                    visibleX2 = False
                    break

            visibleY1 = True
            for i in range(0, y):
                if treeMap[x][i] >= treeHeight:
                    visibleY1 = False
                    break

            visibleY2 = True
            for i in range(y+1, len(treeMap[x])):
                if treeMap[x][i] >= treeHeight:
                    visibleY2 = False
                    break

            if visibleX1 or visibleX2 or visibleY1 or visibleY2:
                result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    treeMap = getTreeMap()
    result = 0

    for x in range(0, len(treeMap)):
        for y in range(0, len(treeMap[x])):
            treeHeight = treeMap[x][y]

            # Check
            visibleX1 = 0
            for i in reversed(range(0, x)):
                visibleX1 += 1
                if treeMap[i][y] >= treeHeight:
                    break

            visibleX2 = 0
            for i in range(x+1, len(treeMap)):
                visibleX2 += 1
                if treeMap[i][y] >= treeHeight:
                    break

            visibleY1 = 0
            for i in reversed(range(0, y)):
                visibleY1 += 1
                if treeMap[x][i] >= treeHeight:
                    break

            visibleY2 = 0
            for i in range(y+1, len(treeMap[x])):
                visibleY2 += 1
                if treeMap[x][i] >= treeHeight:
                    break

            score = visibleX1 * visibleX2 * visibleY1 * visibleY2
            if score > result:
                result = score

    print("Second: {}".format(result))

second()
