def decode(code, lower='L', higher='H', max=127):
	range = { "min": 0, "max": max }

	for ch in list(code):
		if ch == lower:
			range["max"] = ( range["min"] + range["max"] - 1 ) / 2
		if ch == higher:
			range["min"] = ( range["min"] + range["max"] + 1 ) / 2

	return int(range["min"])

def decode_seat(code):
	row = decode(code[:7], 'F', 'B')
	column = decode(code[7:10], 'L', 'R', 7)

	return row * 8 + column

## MAIN

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

seat_ids = []
max_id = 0
min_id = 1000

for line in Lines:
	seat_id = decode_seat(line)
	seat_ids.append(seat_id)
	if max_id < seat_id: max_id = seat_id;
	if min_id > seat_id: min_id = seat_id;

for i in range(min_id, max_id):
	if i not in seat_ids:
		print('Answer:', i)

exit()

## TESTS

print("max_id", max_id)
print("Success:", max_id == 998)

testresult = decode("FBFBBFF", 'F', 'B')
print("FBFBBFF", testresult)
print("Success:", testresult == 44)

testresult = decode("RLR", 'L', 'R', 7)
print("RLR", testresult)
print("Success:", testresult == 5)

testresult = decode_seat("FBFBBFFRLR")
print("FBFBBFFRLR", testresult)
print("Success:", testresult == 357)

testresult = decode_seat("FFFBBBFRRR")
print("FFFBBBFRRR", testresult)
print("Success:", testresult == 119)

testresult = decode_seat("BBFFBBFRLL	")
print("BBFFBBFRLL", testresult)
print("Success:", testresult == 820)
