def getUniqePartEndPosition(text, length):
    for i in range (length, len(text)):
        if len(set(text[i-length:i])) == len(text[i-length:i]):
            return i

# First part

def first():
    with open("data.txt", "r") as file:
        line = file.readline().strip('\n')

    result = getUniqePartEndPosition(line, 4)

    print("First: {}".format(result))

first()

# Second part

def second():

    with open("data.txt", "r") as file:
        line = file.readline().strip('\n')

    result = getUniqePartEndPosition(line, 14)

    print("Second: {}".format(result))

second()
