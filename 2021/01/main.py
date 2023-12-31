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

def second():
	result = 0
	numbers = []

	with open("data.txt", "r") as file:
		line = file.readline()

		while line != "":
			numbers.append(int(line))
			line = file.readline()

			if(len(numbers) > 4):
				numbers.pop(0)
			elif(len(numbers) < 4):
				continue

			if(sum(numbers[:-1]) < sum(numbers[1:])):
				result = result + 1

	print("Second: {}".format(result))

second()
