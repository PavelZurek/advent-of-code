# First part

def first():
    data = []

    with open("data.txt", "r") as file:
        data = list(map(int, file.readline().strip().split(',')))

    for i in range(80):
        for j in range(len(data)):
            data[j] -=1
            
            if data[j] < 0:
                data[j] = 6
                data.append(8)

    result = len(data)
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result)) # Not 950476 (high)

#second()
