import random

class Card:

    def __init__(self, value, suit):
        if suit == 'Червы' or suit == 'Hearts':
            self.suit = '\u2665'
            self.suit_val = 4
        elif suit == 'Бубны' or suit == 'Diamonds':
            self.suit = '\u2666'
            self.suit_val = 3
        elif suit == 'Трефы' or suit == 'Clubs':
            self.suit = '\u2663'
            self.suit_val = 2
        elif suit == 'Пики' or suit == 'Spades':
            self.suit = '\u2660'
            self.suit_val = 1
        else:
            print('Неправильно введена масть!')

        if value == 'J':
            self.value_val = 11
        elif value == 'Q':
            self.value_val = 12
        elif value == 'K':
            self.value_val = 13
        elif value == 'A':
            self.value_val = 14
        else:
            self.value_val = int(value)
        self.value = value
        self.com_view = str(f'{self.value}{self.suit}')

    def to_str(self):
        return self.com_view

    def equal_suit(self, card):
        return True if self.suit_val == card.suit_val else False

    def more(self, card):
        return True if (self.value_val > card.value_val) or (self.value_val == card.value_val and self.suit_val > card.suit_val) else False

    def less(self, card):
        return True if (self.value_val < card.value_val) or (self.value_val == card.value_val and self.suit_val < card.suit_val) else False


card1 = Card(5, 'Diamonds')
print(card1.to_str())
# card2 = Card(4, 'Hearts')
# print(card1.equal_suit(card2))
# print(card1.more(card2))
# print(card1.less(card2))


class Deck:

    def __init__(self):
        self.arr = []
        for j in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for i in range(2, 15):
                if i == 11:
                    i = 'J'
                elif i == 12:
                    i = 'Q'
                elif i == 13:
                    i = 'K'
                elif i == 14:
                    i = 'A'
                card = Card(i, j)
                self.arr.append(card.com_view)

    def shuffle(self):
        random.shuffle(self.arr)
        return self.arr

    def draw(self, num):
        new_arr = []
        for i in range(0, num):
            new_arr.append(self.arr[0])
            self.arr.pop(0)
        return new_arr

    def show(self):
        result = (f'deck[{len(self.arr)}]: ')
        for i in self.arr:
            result += (f'{i}, ')
        return result[0:-2]


deck = Deck()

print(deck.shuffle())
#print(deck.draw(2))

print(deck.show())