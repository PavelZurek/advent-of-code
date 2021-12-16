# First part

def first():
    packet = ''

    with open("data.txt", "r") as file:
        packet = file.readline().strip()

    binary = ''.join(['{:04b}'.format(int(i, 16)) for i in packet])

    transmission = []

    while len(binary) > 0 and len(set(list(binary))) > 1:
        packet = {}

        packet['version'] = int(binary[:3], 2)
        packet['type_id'] = int(binary[3:6], 2)

        if packet['type_id'] == 4:

            offset = 6

            value = ''
            read = True
            while read:
                n = (binary[offset:offset+5])
                offset += 5

                value = '{}{}'.format(value, n[1:])

                if(n[0] == '0'):
                    read = False

            packet['value'] = int(value, 2)
            packet['raw_data'] = binary[:offset]

            binary = binary[offset:]

        else:
            packet['length_type_id'] = int(binary[6:7], 2)

            offset = 18 if packet['length_type_id'] == 1 else 22
            packet['length'] = int(binary[7:offset], 2)

            packet['raw_data'] = binary[:offset]
            binary = binary[offset:]

        transmission.append(packet)

    result = 0
    for packet in transmission:
        result += packet['version']

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
