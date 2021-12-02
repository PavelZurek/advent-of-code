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

max_seat_id = 0

for line in Lines:
	seat_id = decode_seat(line)
	if seat_id > max_seat_id:
		max_seat_id = seat_id

print('Answer:', max_seat_id)

exit()

## TESTS

testresult = decode("FBFBBFF", 'F', 'B')
print(testresult)
print("Success:", testresult == 44)

testresult = decode("RLR", 'L', 'R', 7)
print(testresult)
print("Success:", testresult == 5)
