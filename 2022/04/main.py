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

def second():
    result = 0
    print("Second: {}".format(result))

#second()
