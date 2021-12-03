# First part

def first():
    file = open("data.txt", "r")

    sums = [0 for x in range(0,len(file.readline().strip()))]
    linecount = 0

    for line in file:
        if line == "" or line == '\n':
            break
        linecount = linecount + 1

        for i in range(0,len(line.strip())):
            sums[i] = sums[i] + int(line[i].strip())

    gamma = ''
    epsilon = ''
    for i in sums:
        value = 1 if i > linecount/2 else 0
        gamma = gamma + str(value)
        epsilon = epsilon + str(abs(value - 1))

    result = int(gamma, 2) * int(epsilon, 2)
    print("First: {}".format(result)) # Not 836

first()

# Second part

def getData():
    data = []

    with open("data.txt", "r") as file:

        for line in file:
            if line == "" or line == '\n':
                break

            data.append(line.strip())

    return data

def second():
    data = getData()
    linecount = len(data)
    bit = 0

    while len(data) > 1:
        count_ones = 0
        new_data = []

        for i in range(0, len(data)):
            count_ones = count_ones + int(data[i][bit])

        count_zeros = len(data) - count_ones
        value = 1 if count_ones >= count_zeros else 0

        for i in range(0, len(data)):
            if data[i][bit] == str(value):
                new_data.append(data[i])

        bit = bit + 1
        data = new_data

    oxygen = data[0]

    data = getData()
    bit = 0
    while len(data) > 1:
        count_ones = 0
        new_data = []

        for i in range(0, len(data)):
            count_ones = count_ones + int(data[i][bit])

        count_zeros = len(data) - count_ones
        value = 0 if count_ones >= count_zeros else 1

        for i in range(0, len(data)):
            if data[i][bit] == str(value):
                new_data.append(data[i])

        bit = bit + 1
        data = new_data

    dihydrogen_monoxide = data[0]

    result = int(oxygen, 2) * int(dihydrogen_monoxide, 2)
    print("Second: {}".format(result))

second()
