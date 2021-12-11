pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def checkLine(line, returnFirstInvalidChar=False, returnAutocompletedEnd=False):
    stack = []

    for char in line:
        if char in pairs.keys():
            stack.append(char)
        else:
            char2 = stack.pop()
            
            if pairs[char2] != char:
                if returnFirstInvalidChar:
                    return char
                raise Exception('"{}": Expected {}, but found {} instead.'.format(line, pairs[char2], char))
    
    if len(stack) > 0 and returnAutocompletedEnd:
        ending = []

        while len(stack) > 0:
            char = stack.pop()
            ending.append(pairs[char])
        
        return ''.join(ending)

# First part

error_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break
            
            invalidChar = checkLine(line.strip(), returnFirstInvalidChar=True)
            if(invalidChar):
                result += error_points[invalidChar]

    print("First: {}".format(result))

first()

# Second part

autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def second():
    scores = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            line = line.strip()

            try:
                score = 0
                suffix = checkLine(line, returnAutocompletedEnd=True)

                for suffix_char in suffix:
                    score *= 5
                    score += autocomplete_points[suffix_char]

                scores.append(score)
            except:
                pass

    scores.sort()
    result = scores[int(len(scores)/2)]
    print("Second: {}".format(result))

second()
