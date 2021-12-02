# TODO: north (^), south (v), east (>), or west (<)
# deliver package, repeat(move, deliver)
# How many houses receive at least one present?

inputData = open('input.txt', 'r') 
line = inputData.readline()

santa = 'santa'
robot = 'robot'

coord_x = {}
coord_y = {}
coord_x[santa] = 0
coord_y[santa] = 0
coord_x[robot] = 0
coord_y[robot] = 0
coord_history = []

turn = santa

for char in list(line):
	if   char == '^': coord_x[turn] -= 1;
	elif char == 'v': coord_x[turn] += 1;
	elif char == '>': coord_y[turn] -= 1;
	elif char == '<': coord_y[turn] += 1;
	else: exit();

	coord_history.append('[{}|{}]'.format(coord_x[turn], coord_y[turn]))

	turn = santa if turn == robot else robot

print('Answer: {}'.format(len(set(coord_history))))
