# First part

def getGroupSizes(groups):
    groups = groups.replace('?', '.')
    while '..' in groups: groups = groups.replace('..', '.')
    return [str(len(x)) for x in groups.strip('.').split('.')]

def testGroup(groups, sizes, results):
    if ','.join(getGroupSizes(groups)) == ','.join(sizes):
        results.append(groups.replace('?', '.'))
    for i, ltr in enumerate(groups):
        if ltr == '?':
            subGroups = groups[:i].replace('?', '.') + '#' + groups[i + 1:]
            testGroup(subGroups, sizes, results)

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            groups, sizes = line.strip().split(' ')
            sizes = sizes.split(',')

            results = []
            testGroup(groups, sizes, results)

            result += len(results)

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
