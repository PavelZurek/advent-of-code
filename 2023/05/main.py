# First part

def first():
    with open("data.txt", "r") as file:
        seeds = [{1: int(x)} for x in next(file).strip().split(':')[-1].strip().split(' ')]
        level = 1

        for line in file:
            line = line.strip()

            # Empty line
            # - create new level
            # - replace empty values from previous level
            if len(line) < 1:
                for seed in seeds:
                    seed[level+1] = None
                    if level > 1 and seed[level] == None:
                        seed[level] = seed[level-1]

                next(file)
                level += 1

            # Non-empty line
            # - calculate next level
            else:
                dest_start, source_start, range_length = [int(x) for x in line.split(' ')]
                for seed in seeds:
                    prev_level_value = seed[level-1]
                    if source_start <= prev_level_value <= source_start + range_length and seed[level] == None:
                        diff = source_start - dest_start
                        seed[level] = prev_level_value - diff

        # Fix last level values and find minimum
        result = None
        for seed in seeds:
            value = seed[level-1] if seed[level] == None else seed[level]
            if result == None or value < result:
                result = value

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
