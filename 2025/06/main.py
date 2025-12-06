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
    print("Second: {}".format(result))

#second()
