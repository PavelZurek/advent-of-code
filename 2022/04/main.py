# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            [rangeA, rangeB] = line.strip().split(',')
            [aFrom, aTo] = map(int, rangeA.split('-'))
            [bFrom, bTo] = map(int, rangeB.split('-'))

            # A contains B
            if (aFrom <= bFrom and aTo >= bTo):
                result += 1
            # B contains A, else to not count if A == B
            elif (aFrom >= bFrom and aTo <= bTo):
                result += 1

    print("First: {}".format(result))

first()

# Second part

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

def second():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            [rangeA, rangeB] = line.strip().split(',')
            [aFrom, aTo] = map(int, rangeA.split('-'))
            [bFrom, bTo] = map(int, rangeB.split('-'))

            if len(intersect(list(range(aFrom, aTo+1)), list(range(bFrom, bTo+1)))) > 0:
                result += 1

    print("Second: {}".format(result))

second()
