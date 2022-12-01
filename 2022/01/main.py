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
    result = 0
    print("Second: {}".format(result))

#second()
