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
    ranges = []

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if "-" in line:
                new_range = list(map(int, line.split("-")))

                overlaping_ranges = []
                for range in ranges:
                    if not (new_range[1] < range[0] or new_range[0] > range[1]):
                        overlaping_ranges.append(range)

                if overlaping_ranges:
                    for range in overlaping_ranges:
                        ranges.remove(range)
                        if new_range[0] > range[0]:
                            new_range[0] = range[0]
                        if new_range[1] < range[1]:
                            new_range[1] = range[1]

                ranges.append(new_range)
            else:
                break

    result = 0
    for range in ranges:
        result += range[1] - range[0] + 1

    print("Second: {}".format(result))

second()
