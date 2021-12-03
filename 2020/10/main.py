# First part

def first():
    numbers = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break

            numbers.append(int(line))

    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()
    diffs = [0 for _ in range(3)]

    for i in range(0, len(numbers) - 1):
        diffs[numbers[i+1] - numbers[i] - 1] += 1

    result = diffs[0] * diffs[2]
    print("First: {}".format(result)) # Not 140 (low), 4704 (high)

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
