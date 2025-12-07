# First part

def allIndexesOfChar(str, ch):
    return {v for v, x in enumerate(str) if x == ch}

def first():
    result = 0
    beams = set()

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if len(beams) == 0:
                beams = allIndexesOfChar(line, "S")
            elif "^" in line:
                reflectors = allIndexesOfChar(line, "^")
                reflectors_hit = reflectors.intersection(beams)

                result += len(reflectors_hit)

                new_beams = set()
                for hit in reflectors_hit:
                    new_beams.add(hit-1)
                    new_beams.add(hit+1)
                for beam in beams - reflectors_hit:
                    new_beams.add(beam)

                beams = new_beams

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
