import re

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            numbers = re.sub(r'[^0-9]', '', line)
            number = int(f"{numbers[0]}{numbers[-1]}")
            result += number

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
