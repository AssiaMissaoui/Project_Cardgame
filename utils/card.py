class symbol:
    """Class defining a symbol on the card characterized by:
    -color
    -Icon as single character out of this list [♥, ♦, ♣, ♠]"""

    # Class Attributes
    color = ["black", "red"]
    icon = {"diamonds" : "♦", "Clubs" : "♣", "spades" : "♠", "herats" : "♥"}

    # constructor of this class
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon
        
class card(symbol):
    """Class inherits from symbol with added attribute: value ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']"""

    #Class Attributes
    value = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']

    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

    def __str__(self):
        return f"{self.color}{self.icon}{self.value}"

#c = card("black", '♣', "6")
#print(c)



