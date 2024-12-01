def getLists():
    lists = [[], []]

    with open("data.txt", "r") as file:
        for line in file:
            [a, b] = map(int, line.split('   '))
            lists[0].append(a)
            lists[1].append(b)

    return lists

# First part

def first():
    lists = getLists()
    lists[0].sort()
    lists[1].sort()

    result = 0

    for i in range(0, len(lists[0])):
        result += abs(lists[0][i] - lists[1][i])

    print("First: {}".format(result))

first()

# Second part

def second():
    lists = getLists()
    result = 0

    for i in range(0, len(lists[0])):
        result += lists[0][i] * lists[1].count(lists[0][i])

    print("Second: {}".format(result))

second()
