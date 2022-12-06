# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        line = file.readline().strip('\n')

    for i in range (4, len(line)):
        if len(set(line[i-4:i])) == len(line[i-4:i]):
            result = i
            break

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
