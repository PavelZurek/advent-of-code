# First part

def arePagesValid(rules: dict[int, list[int]], pages: list[int]):
    for key, values in rules.items():
        for value in values:
            if key in pages and value in pages:
                if pages.index(key) > pages.index(value):
                    return False
    return True

def first():
    loadingRules = True
    rules = {}
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                loadingRules = False
            elif loadingRules:
                [key, value] = list(map(int, line.split('|')))
                if key not in rules:
                    rules[key] = []
                rules[key].append(value)
            else:
                pages = list(map(int, line.split(',')))
                if (arePagesValid(rules, pages)):
                    result += pages[int(len(pages)/2)]

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
