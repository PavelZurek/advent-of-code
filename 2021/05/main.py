# First part

def first():
    x1s, x2s, y1s, y2s = [[],[],[],[]]

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break

            x, y = line.strip().split(' -> ')
            x1, y1 = x.split(',')
            x2, y2 = y.split(',')
            x1, x2, y1, y2 = list(map(int, [x1, x2, y1, y2]))

            if x1 == x2 or y1 == y2:
                x1s.append(min(x1, x2))  
                y1s.append(min(y1, y2))
                x2s.append(max(x1, x2))
                y2s.append(max(y1, y2))

    maxX = max([max(x1s), max(x2s)]) + 1
    maxY = max([max(y1s), max(y2s)]) + 1
    diagram = [list(map(int, list('0'*maxY))) for i in range(maxX)]

    for i in range(len(x1s)):
        if x1s[i] == x2s[i]:
            for y in range(y1s[i], y2s[i] + 1):
                diagram[y][x1s[i]] += 1
        elif y1s[i] == y2s[i]:
            for x in range(x1s[i], x2s[i] + 1):
                diagram[y1s[i]][x] += 1                                      

    result = 0
    for dr in diagram:
        for n in dr:
            if n > 1:
                result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
