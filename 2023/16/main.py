class Direction:
    UP = 'up'
    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'

def getCoordsInDirection(coords, direction):
    x, y = coords
    if direction == Direction.UP:
        return [x-1, y]
    if direction == Direction.RIGHT:
        return [x, y+1]
    if direction == Direction.DOWN:
        return [x+1, y]
    if direction == Direction.LEFT:
        return [x, y-1]

def getBeamInDirection(coords, direction):
    coords = getCoordsInDirection(coords, direction)
    return {
        'coords': coords,
        'direction': direction
    }

def coordsNotOutOfBound(field, coords):
    return coords[0] in range(0, len(field)) and coords[1] in range(0, len(field[0]))

def getEnergizedCoords(field, startBeam):
    beamEnds = [startBeam]
    allBeams = [beamEnds[0]]
    allVisitedCoords = [beamEnds[0]['coords']]

    while len(beamEnds):
        newEnds = []

        for beamEnd in beamEnds:
            tile = field[beamEnd['coords'][0]][beamEnd['coords'][1]]
            nextBeams = []

            if tile == '.' or (tile == '|' and beamEnd['direction'] in [Direction.UP, Direction.DOWN]) or (tile == '-' and beamEnd['direction'] in [Direction.RIGHT, Direction.LEFT]):
                nextBeams.append(getBeamInDirection(beamEnd['coords'], beamEnd['direction']))
            elif tile == '|':
                nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.UP))
                nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.DOWN))
            elif tile == '-':
                nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.LEFT))
                nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.RIGHT))
            elif tile == '/':
                if beamEnd['direction'] == Direction.UP:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.RIGHT))
                if beamEnd['direction'] == Direction.RIGHT:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.UP))
                if beamEnd['direction'] == Direction.DOWN:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.LEFT))
                if beamEnd['direction'] == Direction.LEFT:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.DOWN))
            elif tile == '\\':
                if beamEnd['direction'] == Direction.UP:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.LEFT))
                if beamEnd['direction'] == Direction.RIGHT:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.DOWN))
                if beamEnd['direction'] == Direction.DOWN:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.RIGHT))
                if beamEnd['direction'] == Direction.LEFT:
                    nextBeams.append(getBeamInDirection(beamEnd['coords'], Direction.UP))

            for nextBeam in nextBeams:
                if coordsNotOutOfBound(field, nextBeam['coords']):
                    if nextBeam['coords'] not in allVisitedCoords:
                        allVisitedCoords.append(nextBeam['coords'])
                    if coordsNotOutOfBound(field, nextBeam['coords']) and nextBeam not in allBeams:
                        allBeams.append(nextBeam)
                        newEnds.append(nextBeam)

        beamEnds = newEnds

    return allVisitedCoords

# First part

def first():
    field = []

    with open("data.txt", "r") as file:
        for line in file:
            field.append(line.strip())

    energizedCoords = getEnergizedCoords(field, {
        'coords': [0, 0],
        'direction': Direction.RIGHT,
    })

    result = len(energizedCoords)
    print("First: {}".format(result))

first()

# Second part

def second():
    field = []

    with open("data.txt", "r") as file:
        for line in file:
            field.append(line.strip())

    allStartBeams = []
    for i in range(0, len(field)):
        allStartBeams.append({
            'coords': [0, i],
            'direction': Direction.DOWN,
        })
    for i in range(0, len(field)):
        allStartBeams.append({
            'coords': [len(field[i])-1, i],
            'direction': Direction.UP,
        })
    for i in range(0, len(field[0])):
        allStartBeams.append({
            'coords': [i, 0],
            'direction': Direction.RIGHT,
        })
    for i in range(0, len(field[0])):
        allStartBeams.append({
            'coords': [i, len(field)-1],
            'direction': Direction.LEFT,
        })

    result = 0
    for startBeam in allStartBeams:
        length = len(getEnergizedCoords(field, startBeam))
        if length > result:
            result = length

    print("Second: {}".format(result))

second()
