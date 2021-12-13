def getData():
    coordinates = []
    folds = []

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if ',' in line:
                coordinates.append(list(map(int, line.split(','))))

            if '=' in line:
                fold = line.split(' ').pop().split('=')
                folds.append([fold[0], int(fold[1])])

    return coordinates, folds

def getMaxCoords(coordinates):
    maxCoords = list(coordinates[0])

    for coords in coordinates:
        if coords[0] > maxCoords[0]:
            maxCoords[0] = coords[0]
        if coords[1] > maxCoords[1]:
            maxCoords[1] = coords[1]

    return maxCoords

def draw(coordinates, size):
    maxX, maxY = getMaxCoords(coordinates)

    drawing = [list('.'*(size[0]+1)) for _ in range(size[1]+1)]

    for c in coordinates:
        drawing[c[1]][c[0]] = '#'

    for i in range(len(drawing)):
        print(''.join(drawing[i]))

def do_fold(coordinates, fold):
    maxX, maxY = getMaxCoords(coordinates)

    if fold[0] == 'x':
        maxX = fold[1]
    elif fold[0] == 'y':
        maxY = fold[1]

    new_coordinates = []

    for c in coordinates:
        # Keep points on good half
        if c[0] < maxX + 1 and c[1] < maxY + 1:
            if [c[0], c[1]] not in new_coordinates:
                new_coordinates.append(c)
        # Move points from othe half
        else:
            x, y = c
            if fold[0] == 'x':
                x = maxX - (c[0] - maxX)
            elif fold[0] == 'y':
                y = maxY - (c[1] - maxY)
            if [x, y] not in new_coordinates:
                new_coordinates.append([x, y])

    return new_coordinates

# First part

def first():
    coordinates, folds = getData()

    coordinates = do_fold(coordinates, folds[0])

    result = len(coordinates)
    print("First: {}".format(result))

first()

# Second part

def second():
    coordinates, folds = getData()
    size = getMaxCoords(coordinates)

    while len(folds) > 0:
        fold = folds.pop(0)
        coordinates = do_fold(coordinates, fold)
        if fold[0] == 'x':
            size[0] = fold[1] - 1
        if fold[0] == 'y':
            size[1] = fold[1] - 1

    print("Second:")
    draw(coordinates, size)

second()
