def numberrStringToList(ns):
    return ns.replace('  ', ' ').strip(' ').strip('\n').split(' ')

class Card:
    def __init__(self, line):
        [name, numbers] = line.split(':')
        [guessed, win] = numbers.split('|')

        self.tip = numberrStringToList(guessed)
        self.win = numberrStringToList(win)

    def getWinningTip(self):
        return list(set(self.tip).intersection(self.win))

    def getWinningTipCount(self):
        return len(self.getWinningTip())

    def getScore(self):
        return int(pow(2, self.getWinningTipCount() - 1))

# First part

def first():
    result = 0

    with open("data.txt", "r") as file:
        for line in file:
            card = Card(line)
            result += card.getScore()

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    cardsWon = {}

    with open("data.txt", "r") as file:
        cardId = 0
        for line in file:
            cardId += 1
            card = Card(line)
            if cardId not in cardsWon:
                cardsWon[cardId] = 1

            for i in range(0, card.getWinningTipCount()):
                nextCardId = i + cardId + 1
                if nextCardId not in cardsWon:
                    cardsWon[nextCardId] = 1
                if (cardId in cardsWon):
                    cardsWon[nextCardId] += cardsWon[cardId]

            if cardId in cardsWon:
                result += cardsWon.pop(cardId)

    print("Second: {}".format(result))

second()
