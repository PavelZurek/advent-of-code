def intersection(lst1, lst2): 
    return [value for value in lst1 if value in lst2]

def count_sum(group_answers):
	if len(group_answers) < 1:
		return 0
	if len(group_answers) == 1:
		return len(group_answers[0])

	result = list(group_answers[0])

	for i in range(1, len(group_answers)):
		result = intersection(result, list(group_answers[i]))

	return len(result)

## MAIN

inputData = open('input.txt', 'r') 
Lines = inputData.readlines()

yes_sum = 0
group_answers = []

for line in Lines:
	line = line.rstrip()
	if len(line) > 0:
		group_answers.append(line)
	else:
		yes_sum += count_sum(group_answers)
		group_answers = []

yes_sum += count_sum(group_answers)

print('Answer:', yes_sum)
