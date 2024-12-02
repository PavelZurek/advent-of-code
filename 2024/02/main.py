def isReportSafe(levels):
    direction = 1 if levels[0] - levels[1] < 0 else -1
    for i in range(1, len(levels)):
        distance = (levels[i] - levels[i-1]) * direction
        if distance <= 0 or distance > 3:
            return False
    return True

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            levels = list(map(int, line.split(' ')))
            
            if (isReportSafe(levels)):
                result += 1

    print("First: {}".format(result))

first()

# Second part

def isRecordSafeWithDampener(levels):
    for i in range(0, len(levels)):
        if isReportSafe(levels[:i] + levels[i+1 :]):
            return True
    return False

def second():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            levels = list(map(int, line.split(' ')))

            if (isReportSafe(levels)):
                result += 1
            elif isRecordSafeWithDampener(levels):
                result += 1

    print("Second: {}".format(result))

second()
