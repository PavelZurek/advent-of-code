# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            paterns, values = line.strip().split(' | ')
            values = values.split(' ')

            for value in values:
                if len(value) in [2, 3, 4, 7]:
                    result += 1

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            if line == "":
                break

            paterns, values = line.strip().split(' | ')
            paterns = paterns.split(' ')
            values = values.split(' ')

            # maybe not necessary
            for i in range(len(paterns)):
                paterns[i] = ''.join(sorted(paterns[i]))
            for i in range(len(values)):
                values[i] = ''.join(sorted(values[i]))

            translated = {}

            for patern in paterns: # 1, 4, 7, 8
                if len(patern) == 2:
                    translated[1] = patern
                elif len(patern) == 4:
                    translated[4] = patern
                elif len(patern) == 3:
                    translated[7] = patern
                elif len(patern) == 7:
                    translated[8] = patern

            for patern in paterns: # 0, 2, 3, 5, 6, 9
                if patern not in translated.values():

                    if len(patern) == 5: # 2, 3 or 5

                        # 2
                        if len(set(translated[4]) - set(patern)) == 2:
                            translated[2] = patern

                        # 3
                        if len(set(translated[1]) - set(patern)) == 0:
                            translated[3] = patern

                        # 5
                        if len(set(patern) - set(translated[1])) == 4 and len(set(patern) - set(translated[4])) == 2:
                            translated[5] = patern 

                    if len(patern) == 6: # 0, 6 or 9

                        # 0
                        if len(set(patern) - set(translated[4])) == 3 and len(set(patern) - set(translated[7])) == 3:
                            translated[0] = patern

                        # 6
                        if len(set(patern) - set(translated[1])) == 5:
                            translated[6] = patern

                        # 9
                        if len(set(patern) - set(translated[4])) == 2:
                            translated[9] = patern

            row_result = 0
            for value in values:
                for i in translated.keys():
                    if translated[i] == value:
                        row_result = row_result * 10 + i

            result += row_result

    print("Second: {}".format(result))

second()
