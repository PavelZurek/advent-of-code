# First part
def lineToNumbers(line):
    result = line.split(':')[-1].strip()
    while '  ' in result:
        result = result.replace('  ', ' ')
    return [int(x) for x in result.split(' ')]

def first():
    result = 1

    with open("data.txt", "r") as file:
        times = lineToNumbers(next(file))
        distances = lineToNumbers(next(file))
        raceCount = len(times)

        for i in range(0, raceCount):
            holdTimeCount = 0

            time = times[i]
            distance = distances[i]

            for holdTime in range(1, time):
                total = holdTime * (time - holdTime)
                if total > distance:
                    holdTimeCount += 1

            result *= holdTimeCount

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
