# First part

def first():
	horizontal = 0
	depth = 0

	file = open("data.txt", "r")

	for line in file:
		if line == "" or line == '\n':
			break

		parts = line.strip().split(' ')
		
		command = parts[0]
		distance = int(parts[1])

		if command == 'forward':
			horizontal = horizontal + distance
		elif command == 'down':
			depth = depth + distance
		elif command == 'up':
			depth = depth - distance

	print("First: {}".format(horizontal * depth))

first()

# Second part

def second():
	aim = 0
	horizontal = 0
	depth = 0

	file = open("data.txt", "r")

	for line in file:
		if line == "" or line == '\n':
			break

		parts = line.strip().split(' ')
		
		command = parts[0]
		distance = int(parts[1])


		if command == 'down':
			aim = aim + distance
		elif command == 'up':
			aim = aim - distance
		elif command == 'forward':
			horizontal = horizontal + distance
			depth = depth + (aim * distance)

	print("Second: {}".format(horizontal * depth))

second()
