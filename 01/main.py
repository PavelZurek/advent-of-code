# First part

def first():
	result = 0

	file = open("data.txt", "r")
	previous = int(file.readline())

	for line in file:
		if line == "" or line == '\n':
			break

		currentline = int(line)

		if (previous < currentline):
			result = result + 1

		previous = currentline;

	print("First: {}".format(result))

first()

# Second part

def sum(i, numbers):
	suma = 0
	for j in range(i,i+3):
		suma = suma + numbers[j]
	return suma


def second():
	result = 0

	file = open("data.txt", "r")
	numbers = []

	for line in file:
		if line == "" or line == '\n':
			break

		numbers.append(int(line))

	for i in range(0, len(numbers)-3):
		if(sum(i, numbers) < sum(i+1, numbers)):
			result = result + 1


	print("Second: {}".format(result))


second()
