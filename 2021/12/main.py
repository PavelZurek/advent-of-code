def getData():
    data = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            data.append(line.strip().split('-'))

    return data

def getStartingPaths(data):
    possible_paths = []

    for path in data:
        p = list(path)
        if path[0] == 'start':
            possible_paths.append(p)
        elif path[1] == 'start':
            possible_paths.append(list(reversed(p)))

    return possible_paths

# First part

def first():
    data = getData()
    possible_paths = getStartingPaths(data)
    result = 0

    while len(possible_paths) > 0:
        current_path = possible_paths.pop(0)

        for path in data:
            new_path = list(current_path)

            if new_path[-1] == path[0] and (path[1] not in new_path or path[1][0].isupper()):
                new_path.append(path[1])
            elif new_path[-1] == path[1] and (path[0] not in new_path or path[0][0].isupper()):
                new_path.append(path[0])
            else:
                continue

            if new_path[-1] == 'end':
                result += 1
            else:
                possible_paths.append(new_path)

    print("First: {}".format(result))

first()

# Second part

def isPathValid(path):
    char_counts = {}

    for char in path:
        if char not in char_counts.keys():
            char_counts[char] = 0

        char_counts[char] += 1

    found_two = False
    for char in char_counts.keys():
        if (char == 'start' or char == 'end') and char_counts[char] > 1:
            return False
        if not char.isupper():
            if char_counts[char] > 2:
                return False
            if char_counts[char] == 2:
                if found_two:
                    return False
                found_two = True

    return True

def second():
    data = getData()
    possible_paths = getStartingPaths(data)
    result = 0

    while len(possible_paths) > 0:
        current_path = possible_paths.pop(0)

        for path in data:
            new_path = list(current_path)

            if new_path[-1] == path[0]:
                new_path.append(path[1])
            elif new_path[-1] == path[1]:
                new_path.append(path[0])
            else:
                continue

            if not isPathValid(new_path):
                continue

            if new_path[-1] == 'end':
                result += 1
            else:
                possible_paths.append(new_path)

    print("Second: {}".format(result))

second()
