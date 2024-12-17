# First part

class Computer():
    def __init__(self):
        self.registers = [0, 0, 0]
        self.program = []

        with open("data.txt", "r") as file:
            for i in range(len(self.registers)):
                self.registers[i] = int(file.readline().strip().split(':')[1].strip())
            file.readline()
            self.program = list(map(int, file.readline().strip().split(':')[1].strip().split(',')))

    def __str__(self):
        return '\n'.join([
            'Register A: {}'.format(str(self.registers[0])),
            'Register B: {}'.format(str(self.registers[1])),
            'Register C: {}'.format(str(self.registers[2])),
            'Program: {}'.format(','.join(map(str, self.program))),
        ])
    
    def runProgram(self):
        output = []
        instruction_pointer = 0
        while instruction_pointer < len(self.program):
            opcode = self.program[instruction_pointer]
            operand = self.program[instruction_pointer+1]
            combo = operand
            if operand in range(4, 6):
                combo = self.registers[operand - 4]

            if opcode == 0:
                self.registers[0] = int(self.registers[0] / 2 ** combo)

            elif opcode == 1:
                self.registers[1] = self.registers[1] ^ operand

            elif opcode == 2:
                self.registers[1] = combo % 8

            elif opcode == 3:
                if self.registers[0] != 0:
                    instruction_pointer = operand - 2
            elif opcode == 4:
                self.registers[1] = self.registers[1] ^ self.registers[2]

            elif opcode == 5:
                output.append(str(int(combo % 8)))

            elif opcode == 6:
                self.registers[1] = int(self.registers[0] / 2 ** combo)

            elif opcode == 7:
                self.registers[2] = int(self.registers[0] / 2 ** combo)

            instruction_pointer += 2

        return ','.join(output)

def first():
    computer = Computer()
    result = computer.runProgram()
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
