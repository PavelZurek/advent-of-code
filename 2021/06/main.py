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
    data = []

    with open("data.txt", "r") as file:
        data = list(map(int, file.readline().strip().split(',')))
    
    counts = [0 for _ in range(9)]
    for n in data:
        counts[n] += 1

    for i in range(256):
        n = counts.pop(0)
        counts[6] += n
        counts.append(n)

    result = sum(counts)
    print("Second: {}".format(result))

second()
