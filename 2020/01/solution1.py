# TODO: find the two entries that sum to 2020 and then multiply those two numbers together

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

count = 0
for line in Lines:
	for line2 in Lines:
		n1 = int(line)
		n2 = int(line2)
		if (n1 + n2) == 2020:
			print('{} + {} = 2020'.format(n1, n2))
			print('Answer: {}'.format(n1, n2, n1 * n2))
			exit()
