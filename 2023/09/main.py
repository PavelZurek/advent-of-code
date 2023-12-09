def getDifferenceMap(values):
    return [values[x+1] - values[x] for x in range(0, len(values)-1)]

def getHistory(line):
    values = [[int(x) for x in line.strip().split(' ')]]

    while True:
        values.append(getDifferenceMap(values[-1]))
        if ''.join([str(x) for x in set(values[-1])]) == '0':
            return values

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            history = getHistory(line)

            history[-1].append(0)
            for i in reversed(range(1, len(history))):
                newValue = history[i][-1] + history[i-1][-1]
                history[i-1].append(newValue)

            result += history[0][-1]

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            history = getHistory(line)

            history[-1].insert(0, 0)
            for i in reversed(range(1, len(history))):
                newValue = history[i-1][0] - history[i][0]
                history[i-1].insert(0, newValue)

            result += history[0][0]

    print("Second: {}".format(result))

second()
