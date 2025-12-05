# First part

def first():
    result = 0
    ranges = []

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if "-" in line:
                ranges.append(list(map(int, line.split("-"))))
            elif line:
                for range in ranges:
                    if range[0] <= int(line) <= range[1]:
                        result += 1
                        break

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
