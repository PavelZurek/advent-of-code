# TODO: How many passwords are valid

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

def isValid(line):
	first = int(line[0:line.find('-')]) - 1
	second = int(line[line.find('-') + 1:line.find(' ')]) - 1

	symbol = line[line.find(' ') + 1:line.find(':')]
	password = line[line.find(': ') + 2:-1]

	#print('min: {}, max: {}, symbol: {}, password: "{}"'.format(minimum, maximum, symbol, password))

	return password[first] == symbol and password[second] != symbol or password[first] != symbol and password[second] == symbol

# ----------------------------
validCount = 0

for line in Lines:
	if isValid(line):
		validCount += 1

print('Answer: {}'.format(validCount))
