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

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def intersection(self, range: "Range"):
        print('intersection({}, {})'.format(self, range))
        if range.end >= self.start >= range.start:
            print('>>>{} IN {}'.format(self.start, range))
            return Range(self.start, range.end)
        if range.end >= self.end >= range.start:
            print('>>>{} IN {}'.format(self.end, range))
            return Range(range.start, self.end)
        return None

    def __str__(self):
        return "Range({}, {})".format(self.start, self.end)

    __repr__ = __str__

def getRange(start: int, length: int):
    return Range(start, start+length-1)

def second():
    with open("data.txt", "r") as file:
        seeds = []
        level = 1
        seeds_data = [int(x) for x in next(file).strip().split(':')[-1].strip().split(' ')]

        for i in range(0, len(seeds_data), 2):
            range_start, range_length = seeds_data[i:i+2]
            seeds.append({ 1: getRange(range_start, range_length) })

        for seed in seeds:
            print(seed)

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

                #if level > 3:
                #    exit()
                next(file)
                level += 1
                print('--------------------')
                print('----- LEVEL {} ------'.format(level))
                print('--------------------')

            # Non-empty line
            # - calculate next level
            else:
                dest_start, source_start, range_length = [int(x) for x in line.split(' ')]
                source_range = getRange(source_start, range_length)
                dest_range = getRange(dest_start, range_length)
                #print(source_range, dest_range)
                for seed in seeds:
                    prev_level_value = seed[level-1]
                    intersection = source_range.intersection(prev_level_value)
                    print(prev_level_value)
                    if intersection != None:
                        if seed[level] == None:
                            print('{} AND {} => {}'.format(source_range, prev_level_value, intersection))
                            diff = source_start - dest_start
                            seed[level] = Range(intersection.start+diff, intersection.end+diff)
                        else:
                            print('>>>>NOOOOO')
                            exit()

            print('--')

            for seed in seeds:
                print(seed)

        # Fix last level values and find minimum
        result = None
        for seed in seeds:
            value = seed[level-1] if seed[level] == None else seed[level]
            if result == None or value.start < result:
                result = value.start

    print("Second: {}".format(result))

second()
