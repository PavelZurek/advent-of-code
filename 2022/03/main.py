def intersect(a, b):
    result = []

    if (len(a) < len(b)):
        temp = a
        a = b
        b = temp

    for i in range(0, len(a)):
        if (b.__contains__(a[i])):
            result.append(a[i])

    return result

def convertCharToPriority(c):
    value = ord(c) - 38
    if value > 52:
        value -= 58

    return value

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            first = line[0:len(line.strip())//2]
            second = line[len(line.strip('\n'))//2:].strip("\n")

            intersection = intersect(first, second)

            for c in set(intersection):
                result += convertCharToPriority(c)

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0

    with open("data.txt", "r") as file:
        nextLine = file.readline()

        while len(nextLine) > 1:
            intersection = intersect(
                intersect(
                    nextLine.strip("\n"),
                    file.readline().strip("\n")
                ),
                file.readline().strip("\n")
            )
            nextLine = file.readline()

            for c in set(intersection):
                result += convertCharToPriority(c)

    print("Second: {}".format(result))

second()
