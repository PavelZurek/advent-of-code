# First part

def mix(value, secret_number):
    return value ^ secret_number

def prune(secret_number):
    return secret_number % 16777216

def getNextSecretNumber(secret_number):
    #Calculate the result of multiplying the secret number by 64.
    result = secret_number * 64
    # Then, mix this result into the secret number.
    result = mix(result, secret_number)
    # Finally, prune the secret number.
    secret_number = prune(result)

    #Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    result = int(secret_number / 32)
    # Then, mix this result into the secret number.
    result = mix(result, secret_number)
    # Finally, prune the secret number.
    secret_number = prune(result)

    #Calculate the result of multiplying the secret number by 2048.
    result = secret_number * 2048
    # Then, mix this result into the secret number.
    result = mix(result, secret_number)
    # Finally, prune the secret number.
    return prune(result)

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            secret_number = int(line)
            for _ in range(2000):
                secret_number = getNextSecretNumber(secret_number)
            result += secret_number

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
