# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            first = line[0:len(line.strip())//2]
            second = line[len(line.strip('\n'))//2:].strip("\n")

            intersection = []
            for i in range(0, len(first)):
                if (second.__contains__(first[i])):
                    intersection.append(first[i])

            for x in set(intersection):
                value = ord(x) - 38
                if value > 52:
                    value -= 58
                result += value

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

second()
