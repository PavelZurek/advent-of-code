# TODO: north (^), south (v), east (>), or west (<)
# deliver package, repeat(move, deliver)
# How many houses receive at least one present?

inputData = open('input.txt', 'r') 
line = inputData.readline()

coord_x = 0
coord_y = 0
coord_history = []

for char in list(line):
	if   char == '^': coord_x -= 1;
	elif char == 'v': coord_x += 1;
	elif char == '>': coord_y -= 1;
	elif char == '<': coord_y += 1;
	else: exit();

	coord_history.append('[{}|{}]'.format(coord_x, coord_y))

print('Answer: {}'.format(len(set(coord_history))))
