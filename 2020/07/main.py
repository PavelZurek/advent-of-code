# First part

def first():
    rules = []

    with open("data.txt", "r") as file:
        for line in file:
            if line == "" or line == '\n':
                break
    
            parent, contents = line.strip().split(" contain ")
            contents = contents.split(", ")

            rule = { 'name': ' '.join(parent.split(' ')[:-1]), 'content': [] }
            
            for i in range(0, len(contents)):                  
                tmp = contents[i].rstrip('.').split(' ')[:-1]
                if (tmp[0] != 'no'):
                    rule['content'].append({ 'count': int(tmp[0]), 'name': ' '.join(tmp[1:]) })
    
            rules.append(rule)

    old_count = 0;
    valid_colors = ['shiny gold']

    while old_count != len(valid_colors):
        old_count = len(valid_colors)
        for rule in rules:
            for content in rule.get('content'):
                if content.get('name') in valid_colors:
                    if rule.get('name') not in valid_colors:
                        valid_colors.append(rule.get('name'))
                        
    valid_colors.remove('shiny gold')

    result = len(valid_colors)
    print("First: {}".format(result))

first()

# Second part

def second():
	result = 0

	print("Second: {}".format(result))

#second()
