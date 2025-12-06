# First part

def first():
    result = 0
    numbers = []

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            while "  " in line:
                line = line.replace("  ", " ")

            line = line.split(" ")

            if (line[0].isnumeric()):
                numbers.append(list(map(int, line)))
            else:
                for i in range(0, len(line)):
                    col_result = numbers[0][i]
                    if line[i] == "*":
                        for j in range(1, len(numbers)):
                            col_result *= numbers[j][i]
                    if line[i] == "+":
                        for j in range(1, len(numbers)):
                            col_result += numbers[j][i]
                    result += col_result

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    numberlines = []
    operationline = ""

    with open("data.txt", "r") as file:
        for line in file:
            if line.strip().replace(" ", "").isnumeric():
                numberlines.append(line.replace("\n", ""))
            else:
                operationline = line.replace("\n", "")

    numbers = []
    for c in range(len(numberlines[0])+1):
        if c < len(operationline) and operationline[c].strip():
            operation = operationline[c]

        number = ["" for _ in numberlines]
        for i in range(len(numberlines)):
            if c < len(numberlines[i]):
                number[i] += numberlines[i][c]

        number = "".join(number)

        if number.strip().isnumeric():
            numbers.append(int(number.strip()))
        else:
            col_result = numbers[0]
            if operation == "*":
                for i in range(1, len(numbers)):
                    col_result *= numbers[i]
            elif operation == "+":
                for i in range(1, len(numbers)):
                    col_result += numbers[i]
            result += col_result
            numbers = []

    print("Second: {}".format(result))

second()
