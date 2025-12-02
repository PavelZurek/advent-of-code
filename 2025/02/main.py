# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        r = ""
        while True:
            char = file.read(1)
            if not char:
                break
            elif char != ",":
                r += char
            else:
                rFrom, rTo = list(map(int, r.strip().split('-')))
                r = ""

                for id in range(rFrom, rTo+1):
                    strId = str(id)
                    if len(strId) % 2 == 0 and strId[:len(strId)//2] == strId[len(strId)//2:]:
                        result += id

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
