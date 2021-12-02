# TODO: How many passwords are valid

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

def isValid(line):
	minimum = int(line[0:line.find('-')])
	maximum = int(line[line.find('-') + 1:line.find(' ')])

	symbol = line[line.find(' ') + 1:line.find(':')]
	password = line[line.find(': ') + 2:-1]

	#print('min: {}, max: {}, symbol: {}, password: "{}"'.format(minimum, maximum, symbol, password))

	return minimum <= password.count(symbol) and maximum >= password.count(symbol)

# ----------------------------
validCount = 0

for line in Lines:
	if isValid(line):
		validCount += 1

print('Answer: {}'.format(validCount))
