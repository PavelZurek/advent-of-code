def getPoints():
    x1s, x2s, y1s, y2s = [[],[],[],[]]

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break

            x, y = line.strip().split(' -> ')
            x1, y1 = x.split(',')
            x2, y2 = y.split(',')
            x1, x2, y1, y2 = list(map(int, [x1, x2, y1, y2]))

            x1s.append(x1)  
            y1s.append(y1)
            x2s.append(x2)
            y2s.append(y2)

    return [x1s, x2s, y1s, y2s]

def getDiagram(x1s, x2s, y1s, y2s, countDiagonals=False):
    maxX = max([max(x1s), max(x2s)]) + 1
    maxY = max([max(y1s), max(y2s)]) + 1
    diagram = [list(map(int, list('0'*maxY))) for i in range(maxX)]

    for i in range(len(x1s)):
        if x1s[i] == x2s[i]:
            rng = range(y1s[i], y2s[i] + 1) if y1s[i] < y2s[i] else range(y2s[i], y1s[i] + 1)
            for y in rng:
                diagram[y][x1s[i]] += 1
        elif y1s[i] == y2s[i]:
            rng = range(x1s[i], x2s[i] + 1) if x1s[i] < x2s[i] else range(x2s[i], x1s[i] + 1)
            for x in rng:
                diagram[y1s[i]][x] += 1
        elif countDiagonals:
            stepX = 1 if x1s[i] < x2s[i] else -1
            stepY = 1 if y1s[i] < y2s[i] else -1

            for j in range(abs(x1s[i] - x2s[i]) + 1):
                diagram[y1s[i] + stepY * j][x1s[i] + stepX * j] += 1

    return diagram

def getResult(diagram):
    result = 0

    for dr in diagram:
        for n in dr:
            if n > 1:
                result += 1
                
    return result

# First part

def first():
    x1s, x2s, y1s, y2s = getPoints()
    diagram = getDiagram(x1s, x2s, y1s, y2s)

    result = getResult(diagram)
    print("First: {}".format(result))

first()

# Second part

def second():
    x1s, x2s, y1s, y2s = getPoints()
    diagram = getDiagram(x1s, x2s, y1s, y2s, True)

    result = getResult(diagram)
    print("Second: {}".format(result)) # Not 950476 (high)

second()
