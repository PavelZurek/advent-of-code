# First part

def first():
    lists = [[], []]

    with open("data.txt", "r") as file:
        for line in file:
            [a, b] = map(int, line.split('   '))
            lists[0].append(a)
            lists[1].append(b)

    lists[0].sort()
    lists[1].sort()

    result = 0

    for i in range(0, len(lists[0])):
        result += abs(lists[0][i] - lists[1][i])

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
