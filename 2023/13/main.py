# First part

def findMirrorRow(mirrorMap):
    #for row in mirrorMap:
    #    print(row)

    for i in range(1, len(mirrorMap)):
        isReflection = False

        if mirrorMap[i] == mirrorMap[i-1]:
            isReflection = True
            print(f"Testing index {i}")

            for j in range(0, i-1):
                #print('i', i)
                if i+j+1 >= len(mirrorMap): break
                if i-j < 0: break
                print(f"[{i+j+1}] {mirrorMap[i+j]} vs [{i-j}] {mirrorMap[i-j-1]}")
                if not mirrorMap[i+j] == mirrorMap[i-j-1]:
                    #print(i)
                    isReflection = False
                    break

            if isReflection:
                return i

    return None

def findMirror(mirrorMap):
    mirrorRow = findMirrorRow(mirrorMap)

    if not mirrorRow == None:
        return ['row', mirrorRow]
    else:
        rotatedMirrorMap = [''.join([mirrorMap[j][i] for j in range(len(mirrorMap))]) for i in range(len(mirrorMap[0]))]
        mirrorColumn = findMirrorRow(rotatedMirrorMap)
        if not mirrorColumn == None:
            return ['column', mirrorColumn]

    #for row in rotatedMirrorMap:
    #    print(row)
    #print()
    #for row in mirrorMap:
    #    print(row)
    #print('-----------------------------')

    return ['none', 1]

def first():
    counts = {
        'row': 0,
        'column': 0,
        'none': 0
    }

    with open("data.txt", "r") as file:
        mirrorMap = []

        while True:
            try:
                line = next(file).strip()

                if len(line):
                    mirrorMap.append(line)
                else:
                    kind, index = findMirror(mirrorMap)
                    counts[kind] += index
                    #print(kind, index)
                    mirrorMap = []
            except StopIteration:
                kind, index = findMirror(mirrorMap)
                counts[kind] += index
                #print(kind, index)
                break

    print(counts)

    result = counts['row'] * 100 + counts['column']
    print("First: {}".format(result))
    if result <= 31144: print('LOW!!!')
    if result >= 34177: print('HIGH!!!')

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
