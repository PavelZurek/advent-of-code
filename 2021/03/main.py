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

def second():
    result = 0

    print("Second: {}".format(result))

second()
