# TODO: count all the trees you would encounter for the slope right 3, down 1

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

treeCount = 0;
tree = '#'

top = 0
left = 0

for line in Lines:
	if (left >= (len(line) - 1)):
		left -= (len(line) - 1)

	#print(line, end='')
	#print(' ' * (left), end='')
	#print('^')
	#print(line[left:left+1])

	if line[left:left+1] == tree:
		treeCount += 1

	left += 3

print('Answer: {}'.format(treeCount))
