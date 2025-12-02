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

def getIvalidSum(rFrom, rTo):
    result = 0
    for id in range(rFrom, rTo+1):
        strId = str(id)
        for i in range(1, len(strId)//2+1):
            if strId == strId[:i] * (len(strId)//i):
                result += id
                break
    return result
               

def second():
    result = 0

    with open("data.txt", "r") as file:
        r = ""
        while True:
            nextChar = file.read(1)

            if nextChar and nextChar != ",":
                r += nextChar
            else:
                rFrom, rTo = list(map(int, r.strip().split('-')))
                r = ""
                result += getIvalidSum(rFrom, rTo)

                if not nextChar:
                    break

    print("Second: {}".format(result))

second()
