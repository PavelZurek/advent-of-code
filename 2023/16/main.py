# First part

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

def first():
    field = []

    with open("data.txt", "r") as file:
        for line in file:
            field.append(line.strip())

    beamEnds = [
        {
            'coords': [0, 0],
            'direction': Direction.RIGHT,
        }
    ]

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

    result = len(allVisitedCoords)
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
