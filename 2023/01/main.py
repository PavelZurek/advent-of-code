import re

def lineToNumber(line):
    numbers = re.sub(r'[^0-9]', '', line)
    number = int(f"{numbers[0]}{numbers[-1]}")
    return number

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            result += lineToNumber(line)

    print("First: {}".format(result))

first()

# Second part

numbersAsString = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def second():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            numberIndexes = {}

            for s in numbersAsString.keys():
                numberIndex = [i for i in range(len(line)) if line.startswith(s, i)]
                for ni in numberIndex:
                    numberIndexes[ni] = s

            if len(numberIndexes) > 0:
                replaces = (sorted(numberIndexes.items()))
                replaces = dict([replaces[0], replaces[-1]])

                for index in replaces:
                    stringNumber = replaces[index]
                    numberNumber = numbersAsString[stringNumber]

                    line = line[:index] + numberNumber + line[index + 1:]

            result += lineToNumber(line)

    print("Second: {}".format(result))

second()
