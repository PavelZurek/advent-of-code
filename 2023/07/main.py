from functools import cmp_to_key

# First part

cards = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))

class Hand:
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

class Player:
    def __init__(self, line):
        hand, bid = line.split(' ')
        self.hand = hand
        self.bid = int(bid)

    def getHandKind(self):
        card_counts = {}
        for card in self.hand:
            if card not in card_counts:
                card_counts[card] = 0
            card_counts[card] += 1

        card_count_values = list(card_counts.values())

        if 5 in card_count_values:
            return Hand.FIVE_OF_A_KIND
        if 4 in card_count_values:
            return Hand.FOUR_OF_A_KIND
        if 2 in card_count_values and 3 in card_count_values:
            return Hand.FULL_HOUSE
        if 3 in card_count_values:
            return Hand.THREE_OF_A_KIND

        for i in range(0, len(card_count_values)):
            for j in range(i, len(card_count_values)):
                if not i == j and card_count_values[i] > 1 and card_count_values[i] == card_count_values[j]:
                    return Hand.TWO_PAIRS

        if 2 in card_count_values:
            return Hand.ONE_PAIR
        return Hand.HIGH_CARD

def compareHands(a: Player, b: Player):
    aKind, bKind = [a.getHandKind(), b.getHandKind()]
    if not aKind == bKind:
        return bKind - aKind

    for i in range(0, len(a.hand)):
        if not a.hand[i] == b.hand[i]:
            return cards.index(b.hand[i]) - cards.index(a.hand[i])

    return 0

def first():
    players = []

    with open("data.txt", "r") as file:
        for line in file:
            player = Player(line.strip())
            players.append(player)

    result = 0

    players.sort(key=cmp_to_key(compareHands))
    for i, p in enumerate(players):
        rank = len(players) - i
        result += rank * p.bid

    print("First: {}".format(result))

first()

# Second part

def second():
    result = 0
    print("Second: {}".format(result))

#second()
