# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            bank = line.strip()
            max = int(bank[:2])
            for i in range(0, len(bank)-1):
                for j in range(i+1, len(bank)):
                    value = int(bank[i]+bank[j])
                    if value > max:
                        max = value
            result += max

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
