# TODO: find the three entries that sum to 2020 and then multiply those two numbers together

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

count = 0
for line1 in Lines:
	for line2 in Lines:
		for line3 in Lines:
			n1 = int(line1)
			n2 = int(line2)
			n3 = int(line3)

			if (n1 + n2 + n3) == 2020:
				print('{} + {} + {} = 2020'.format(n1, n2, n3))
				print('Answer: {}'.format(n1, n2, n3, n1 * n2 * n3))
				exit()
