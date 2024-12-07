def testEquationVariation(result, values, bin_variations):
    operations = list('+' * (len(values)-1))
    for i in range(len(operations)):
        if i in range(len(bin_variations)):
            if bin_variations[-i] == '1':
                operations[-i] = '*'
            elif bin_variations[-i] == '2':
                operations[-i] = '||'

    test_result = values[0]
    for i in range(1, len(values)):
        if operations[i-1] == '+':
            test_result += values[i]
        elif operations[i-1] == '*':
            test_result *= values[i]
        else:
            test_result = int('{}{}'.format(test_result, values[i]))

    return result == test_result

# First part

def isEquationValid(result, values):
    bin_variations_len = len(values) - 1
    variations = pow(2, bin_variations_len)
    for i in range(0, variations):
        bin_variations = format(i, '0{}b'.format(bin_variations_len))
        if testEquationVariation(result, values, bin_variations):
            return True
    return False

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            values = line.strip().split(': ')
            test_value = int(values[0])
            values = list(map(int, values[1].split(' ')))

            if isEquationValid(test_value, values):
                result += test_value

    print("First: {}".format(result))

first()

# Second part

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def isSecondEquationValid(result, values):
    bin_variations_len = len(values) - 1
    variations = pow(3, bin_variations_len)
    for i in range(0, variations):
        variation = ternary(i)
        variation = '0' * (bin_variations_len - len(variation)) + variation
        if testEquationVariation(result, values, variation):
            return True
    return False

def second():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            values = line.strip().split(': ')
            test_value = int(values[0])
            values = list(map(int, values[1].split(' ')))

            if isSecondEquationValid(test_value, values):
                result += test_value

    print("Second: {}".format(result))

second()
