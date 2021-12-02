def count_sum(answers):
	return len(set(list(answers)))

## MAIN

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

yes_sum = 0
group_answers = ""

for line in Lines:
	line = line.rstrip()
	if len(line) > 0:
		group_answers = group_answers + line
	else:
		yes_sum += count_sum(group_answers)
		group_answers = ""

yes_sum += count_sum(group_answers)

print('Answer:', yes_sum)
