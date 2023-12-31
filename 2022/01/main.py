# First part

def first():
    result = 0

    file = open("data.txt", "r")

    current_sum = 0

    for line in file:
        if line == "" or line == '\n':
            if current_sum > result:
                result = current_sum
            current_sum = 0
        else:
            current_sum += int(line)

    print("First: {}".format(result))

first()

# Second part

def second():
    file = open("data.txt", "r")

    current_sum = 0
    top = [0, 0, 0]

    for line in file:
        if line == "" or line == '\n':
            if top[0] < current_sum:
                top.pop(0)
                top.append(current_sum)
                top.sort()
            current_sum = 0
        else:
            current_sum += int(line)

    result = top[0]+top[1]+top[2]
    print("Second: {}".format(result))

second()
