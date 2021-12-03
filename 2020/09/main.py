# First part

def first(print_result=True):
    window_size = 25 + 1
    window = []
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break

            current = int(line)
            window.append(current)

            if len(window) > window_size:
                window.pop(0)
            elif len(window) < window_size:
                continue

            preamble, current = [window[:-1], window[-1:][0]]

            found = False
            for i in preamble:
                x = current - i
                if x in preamble:
                    found = True
            
            if not found:
                result = current
                break;  

    if print_result:
        print("First: {}".format(result))

    return result

first()

# Second part

def second():
    data = []
    invalid_number = first(False)
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break

            data.append(int(line))

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if sum(data[i:j+1]) == invalid_number:
                result = min(data[i:j+1]) + max(data[i:j+1])
    
    print("Second: {}".format(result))

second()
