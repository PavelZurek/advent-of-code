# First part

def first():
    with open("data.txt", "r") as file:
        stateLines = []

        # save instructions
        line = file.readline().strip('\n')
        while line.strip()[0] == '[': # reading starting state
            stateLines.append(line)
            line = file.readline().strip('\n')

        # line now contains column numbers
        lines = line.strip().split("   ")

        # create empty state
        currentState = {}
        for lineNumber in lines:
            currentState[lineNumber] = []

        # fill current state
        for stateLine in reversed(stateLines):
            for col in range(0, len(currentState)):
                cartId = stateLine[col*4+1:col*4+2]
                if (cartId.strip() != ""):
                    stateKey = "{}".format(col+1)
                    currentState[stateKey].append(cartId)

        #print(currentState)

        # empty row to divide state and instructions
        file.readline()

        # calculate instructions
        line = file.readline().strip(" \n")
        while line != "":
            # parse instruction
            [_, x, _, f, _, t] = line.split(' ')
            for i in range (0, int(x)):
                cartId = currentState[f].pop()
                currentState[t].append(cartId)

            line = file.readline().strip(" \n")

    # calculate result
    result = []

    for col in currentState:
        result.append(currentState[col][-1])

    print("First: {}".format(''.join(result)))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
