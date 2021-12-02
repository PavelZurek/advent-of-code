# TODO: Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

required_fields = [
    "byr", #(Birth Year) - four digits; at least 1920 and at most 2002.
    "iyr", #(Issue Year) - four digits; at least 2010 and at most 2020.
    "eyr", #(Expiration Year) - four digits; at least 2020 and at most 2030.
    "hgt", #(Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
    "hcl", #(Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "ecl", #(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "pid", #(Passport ID) - a nine-digit number, including leading zeroes.
#    "cid", #(Country ID) - ignored, missing or not.
]

def validatePassport(fields):
	for required_field in required_fields:
		if required_field not in fields:
			return False

	if int(fields["byr"]) < 1920 or int(fields["byr"]) > 2002:
		return False

	if int(fields["iyr"]) < 2010 or int(fields["iyr"]) > 2020:
		return False

	if int(fields["eyr"]) < 2020 or int(fields["eyr"]) > 2030:
		return False

	hgt_value = fields["hgt"][:-2]
	hgt_unit = fields["hgt"][len(hgt_value):]
	if hgt_unit == 'cm':
		if (150 > int(hgt_value) or int(hgt_value) > 193):
			return False
	elif hgt_unit == 'in':
		if (59 > int(hgt_value) or int(hgt_value) > 76):
			return False
	else:
		return False

	if len(fields["hcl"]) != 7 or fields["hcl"][:1] != '#' or not set(fields["hcl"][1:]).issubset(set('0123456789abcdef')):
		return False

	if fields["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False

	if len(fields["pid"]) != 9 or not fields["pid"].isdecimal():
		return False

	return True

## MAIN

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

valid_count = 0
fields = {};

for line in Lines:
	props = line.replace("\n", "").split(' ')

	if(len(line.replace('\n', '')) < 1):
		if (validatePassport(fields)):
			valid_count += 1
		#	print('Valid ', fields)
		#else:
		#	print('Invalid ', fields)
		fields = {}
	else:
		for prop in props:
			[name, value] = prop.split(':')
			fields[name] = value



print('Answer: {}'.format(valid_count))
