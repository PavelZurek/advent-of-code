# First part

def first():
    result = 0
    dial = 50

    with open("data.txt", "r") as file:
        for line in file:
            dial_move = int(line[1:])
            if line[0] == 'L':
                dial -= dial_move
                while dial < 0:
                    dial += 100
            elif line[0] == 'R':
                dial += dial_move
                while dial > 99:
                    dial -= 100

            if dial == 0:
                result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    dial = 50

    with open("data.txt", "r") as file:
        for line in file:
            dial_move = int(line[1:])

            if line[0] == 'L':
                result += (dial-1)//100 - (dial-dial_move-1)//100
                dial -= dial_move
            elif line[0] == 'R':
                result += (dial+dial_move)//100 - dial//100
                dial += dial_move

            dial = dial%100

    print("Second: {}".format(result))

second()
