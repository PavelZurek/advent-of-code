# First part

ROCK = 1
PAPPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            [op, my] = line.split()
            op = ord(op)-64
            my = ord(my)-87

            result += my

            if (op == my):
                result += DRAW
            if (op == ROCK and my == PAPPER):
                result += WIN
            if (op == PAPPER and my == SCISSORS):
                result += WIN
            if (op == SCISSORS and my == ROCK):
                result += WIN

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

second()
