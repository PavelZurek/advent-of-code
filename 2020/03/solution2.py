# TODO: count all the trees you would encounter for the slopes:
#    Right 1, down 1.
#    Right 3, down 1. (This is the slope you already checked.)
#    Right 5, down 1.
#    Right 7, down 1.
#    Right 1, down 2.
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

tree = '#'

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

def countTrees(right, down):
	treeCount = 0;

	top = down
	left = right

	while top < len(Lines):
		line = Lines[top]

		if (left >= (len(line) - 1)):
			left -= (len(line) - 1)

		#print(line, end='')
		#print(' ' * (left), end='')
		#print('^')
		#print(line[left:left+1])

		if line[left:left+1] == tree:
			treeCount += 1

		left += right
		top += down

	return treeCount


#print('Right 1, down 1: {} trees.'.format(countTrees(1, 1)))
#print('Right 3, down 1: {} trees.'.format(countTrees(3, 1)))
#print('Right 5, down 1: {} trees.'.format(countTrees(5, 1)))
#print('Right 7, down 1: {} trees.'.format(countTrees(7, 1)))
#print('Right 1, down 2: {} trees.'.format(countTrees(1, 2)))
print(
	'Answer: {}'.format(
		countTrees(1, 1)*countTrees(3, 1)*countTrees(5, 1)*countTrees(7, 1)*countTrees(1, 2)
	)
)
