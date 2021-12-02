# TODO: Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

required_fields = [
    "byr", #(Birth Year)
    "iyr", #(Issue Year)
    "eyr", #(Expiration Year)
    "hgt", #(Height)
    "hcl", #(Hair Color)
    "ecl", #(Eye Color)
    "pid", #(Passport ID)
#    "cid", #(Country ID)
]
fields = {};

valid_count = 0

def validatePassport(fields):
	for required_field in required_fields:
		if required_field not in fields:
			return False
	return True


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
