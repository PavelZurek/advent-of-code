# First part

def first():
    disk = []

    with open("data.txt", "r") as file:
        diskmap = file.read().strip()

        readFile = True
        fileId = 0
        for i in range(len(diskmap)):
            number = int(diskmap[i])
            if readFile:
                for _ in range(number):
                    disk.append(str(fileId))
                fileId += 1
            else:
                for _ in range(number):
                    disk.append('.')

            readFile = not readFile

    change = True
    while change:
        change = False

        firstSpace = None
        lastFile = None

        for i in range(int(len(disk))):
            minusI = len(disk)-i-1
            if disk[i] == '.' and firstSpace == None:
                firstSpace = i
            if disk[minusI] != '.' and lastFile == None:
                lastFile = minusI
            if firstSpace != None and lastFile != None:
                break

        if firstSpace < lastFile:
            tmp = disk[firstSpace]
            disk[firstSpace] = disk[lastFile]
            disk[lastFile] = tmp
            change = True

    result = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            break
        result += int(disk[i]) * i

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
