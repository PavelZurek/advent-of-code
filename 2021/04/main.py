# First part

def loadData():
    called_numbers = []
    boards = []

    with open("data.txt", "r") as file:
        called_numbers = file.readline().strip().split(',')
        file.readline()

        board = []
        while True:
            line = file.readline().strip()

            if line == "":
                if len(board) < 1:
                    break
                boards.append(board)
                board = []
            else:     
                board.append(line.replace('  ', ' ').split(' ') )

    return [called_numbers, boards]

def isBoardWinning(board):
    cols = ['' for _ in range(len(board[0]))]

    for i in range(len(board)):
        if ''.join(board[i]) == 'XXXXX':
            return True

        for j in range(len(board[i])):
            cols[j] += board[i][j]
            if cols[j] == 'XXXXX':
                return True

    return False

def getWinningBoard():
    called_numbers, boards = loadData()

    for num in called_numbers:
        for bn in range(len(boards)):
            for i in range(len(boards[bn])):
                for j in range(len(boards[bn][i])):
                    if boards[bn][i][j] == num:
                        boards[bn][i][j] = 'X'
                        if isBoardWinning(boards[bn]):
                            return [boards[bn], num]

def first():
    board, num = getWinningBoard()
    
    board_sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].isdigit():
                board_sum += int(board[i][j])

    result = board_sum * int(num)
    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

second()
