input = []

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

for line in Lines:
	input.append(line[:10])

def parse_boarding_pass(boarding_pass):
    row = boarding_pass[:7].replace('F', '0').replace('B', '1')
    column = boarding_pass[7:].replace('L', '0').replace('R', '1')
    return int(row, 2), int(column, 2)
def seat_id(row, column):
    return row * 8 + column
# STAR 1
max(map(lambda x: seat_id(*x), map(parse_boarding_pass, input)))
# STAR 2
from collections import defaultdict
seats = defaultdict(set)
list(map(lambda x: seats[x[0]].add(x[1]), map(parse_boarding_pass, input)))
min_row, max_row = min(seats.keys()), max(seats.keys())
missing_seats = [(r, c) for r in range(min_row + 1, max_row) for c in range(0, 8) if c not in seats[r]]
print(missing_seats[0])
print(seat_id(*missing_seats[0]))