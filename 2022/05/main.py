def getInitialState(file):
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

    # empty row to divide state and instructions
    file.readline()

    return currentState

def getResult(currentState):
    result = []
    for col in currentState:
        result.append(currentState[col][-1])

    return ''.join(result)

# First part

def first():
    with open("data.txt", "r") as file:
        # load the state
        currentState = getInitialState(file)

        # calculate instructions
        line = file.readline().strip(" \n")
        while line != "":
            # parse instruction
            [_, x, _, f, _, t] = line.split(' ')
            for i in range (0, int(x)):
                cartId = currentState[f].pop()
                currentState[t].append(cartId)

            # read next line
            line = file.readline().strip(" \n")

    print("First: {}".format(getResult(currentState)))

first()

# Second part

def second():
    with open("data.txt", "r") as file:
        # load the state
        currentState = getInitialState(file)

        # calculate instructions
        line = file.readline().strip(" \n")
        while line != "":
            # parse instruction
            [_, x, _, f, _, t] = line.split(' ')
            cartIds = currentState[f][-int(x):]
            currentState[f] = currentState[f][0:-int(x)]
            for cartId in cartIds:
                currentState[t].append(cartId)

            # read next line
            line = file.readline().strip(" \n")

    print("Second: {}".format(getResult(currentState)))

second()
