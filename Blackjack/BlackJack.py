import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):

        for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for v in range(1,14):
                if v == 1:
                    self.cards.append(Card(s, "A"))
                elif v == 11:
                    self.cards.append(Card(s, "J"))
                elif v == 12:
                    self.cards.append(Card(s, "Q"))
                elif v == 13:
                    self.cards.append(Card(s, "K"))
                else:
                    self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.scoreAce = 0
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for c in self.hand:
            c.show()


    def scoreHand(self):
        hasAce = False
        for c in self.hand:
            if c.value == "A":
                self.score += 1
                self.scoreAce += 11
                hasAce = True
            elif c.value in ["J","Q","K"]:
                self.score += 10
                self.scoreAce += 10
            else:
                self.score += c.value
                self.scoreAce += c.value
        if hasAce:
            print(f"The current hand is {self.score} or {self.scoreAce}")
        else:
            print(f"The current hand is {self.score}")


deck = Deck()
deck.shuffle()

travis = Player("Travis")

travis.draw(deck)
travis.draw(deck)

travis.showHand()
travis.scoreHand()





