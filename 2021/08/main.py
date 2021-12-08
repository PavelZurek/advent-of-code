# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            paterns, values = line.strip().split(' | ')
            values = values.split(' ')

            for value in values:
                if len(value) in [2, 3, 4, 7]:
                    result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
