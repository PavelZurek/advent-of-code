# First part

def recalculateParentSizes(node):
    node["size"] = 0
    for childKey in node["children"]:
        childNode = node["children"][childKey]
        if type(childNode) == int:
            node["size"] += childNode
        else:
            node["size"] += childNode["size"]

    if "parent" in node.keys():
        recalculateParentSizes(node["parent"])

def addAllDirSizesAbove(node, above = 100000):
    totalSize = 0

    if node["size"] < above:
        totalSize = node["size"]

    for childKey in node["children"]:
        childNode = node["children"][childKey]
        if type(childNode) != int:
            totalSize += addAllDirSizesAbove(childNode)

    return totalSize

def first():
    tree = {
        "size": 0,
        "children": {}
    }
    cursor = tree

    # Load file tree structure
    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip(" \n").split(' ')

            # Ignore empty lines
            if len(line) == 0:
                continue
            # Dirs from cd commands
            elif line[0] == '$':
                if line[1] == "cd":
                    if line[2] == '/':
                        cursor = tree
                    elif line[2] == "..":
                        cursor = cursor["parent"]
                    else:
                        if line[2] not in cursor["children"].keys():
                            cursor["children"][line[2]] = {
                                "parent": cursor,
                                "size": 0,
                                "children": {}
                            }
                            cursor = cursor["children"][line[2]]
            # Files
            elif line[0] != "dir":
                # Add file to current dir
                cursor["children"][line[1]] = int(line[0])

                # Recalculate sizes of all parents
                recalculateParentSizes(cursor)

    result = addAllDirSizesAbove(tree)
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
