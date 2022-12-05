ROCK = 1
PAPPER = 2
SCISSORS = 3

WIN_SCORE = 6
DRAW_SCORE = 3

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            [op, my] = line.split()
            op = ord(op)-64
            my = ord(my)-87

            result += my

            if (op == my):
                result += DRAW_SCORE
            if (op == ROCK and my == PAPPER):
                result += WIN_SCORE
            if (op == PAPPER and my == SCISSORS):
                result += WIN_SCORE
            if (op == SCISSORS and my == ROCK):
                result += WIN_SCORE

    print("First: {}".format(result))

first()

# Second part

def second():
    WIN = 3
    DRAW = 2
    LOSS = 1

    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            [op, r] = line.split()
            op = ord(op)-64
            r = ord(r)-87

            if (r == DRAW):
                result += op + DRAW_SCORE
            elif (r == WIN):
                result += WIN_SCORE
                if (op == ROCK):
                    result += PAPPER
                if (op == PAPPER):
                    result += SCISSORS
                if (op == SCISSORS):
                    result += ROCK
            else:
                if (op == ROCK):
                    result += SCISSORS
                if (op == PAPPER):
                    result += ROCK
                if (op == SCISSORS):
                    result += PAPPER

    print("Second: {}".format(result))

second()
