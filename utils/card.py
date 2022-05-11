class symbol:
    """Class defining a symbol on the card characterized by:
    -color
    -Icon as single character out of this list[♥, ♦, ♣, ♠]"""

# Class Attributes
red = 'red'
black = 'black' 
hearts = 'hearts'
diamonds = 'diamond'
spades = 'spades'
clubs = 'clubs'

#constructors
    def __init__(self, color):
        self.color = color
        
    def __init__(self, icon):
        self.icon = 