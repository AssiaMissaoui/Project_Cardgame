from card import card

class player:
    """Class defining a symbol on the card characterized by:
    -cards
    -turn_count
    -number_of_cards
    -history"""

    # constructor of this class
    def __init__(self, name: str):
        self.name = name
        self.cards = []
        self.turn_count = 0 
        self.number_of_cards = 0
        self.history = []

    def play(self):
        number = int(input("{}left, choose new card".format(0)))
        card = self.cards[number]
        self.history = [card]
        print(self.name,self.turn_count)
        self.turn_count += 1
        self.history +=[card]
        print(self.number_of_cards)
        print(card)
        return card

class Deck: 
    #attribute of this class
    def __init__(self):
        self.cards = []

    #method that fills the cards
    def fill_deck(self):
        for b in ["♥", "♦", "♣", "♠"]: 
            for d in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(card ("black", b,d))
        


    #method that shuffles the cards
    def shuffle(self):
        shuffle(self.cards)

    #distribute between all players
    #def distribute(self, list_of_players : list):
d = Deck()
d.fill_deck()
print(len(d.cards))