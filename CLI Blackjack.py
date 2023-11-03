# Blackjack
# Karten A, 2, 3, 4, 5, 6, 7, 8, 9, 10, Bube, Dame, König
# Bis 21
# Random Anfangskarte



# Imports
import random
# Variablen
print("// Blackjack von Lou! \\\ ")

cardNames = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Prince', 'Queen', 'King']

# Functions
def randomCard():
    card = random.randint(1, 13)
    return card, cardNames[card - 1]

def printCards():
    if You.newDeal:
        print("||You: ", cardNames[You.currentCard])
        print("||Dealer: ?")
        You.newDeal = False
    else:
        print("||You:", You.currentCard)
        print("||Dealer: ", Dealer.currentCard)
        
def hitOrStand():
    return int(input("Hit(1) or Stand(2)?: "))

def game():
    printCards()
    if hitOrStand() == 1: # hit = you
        You.currentCard = You.currentCard + randomCard()[0]
    else: # hit = dealer
        Dealer.curenntCard = Dealer.currentCard + randomCard()[0]
        if check() == 0:
            if You.currentCard > Dealer.currentCard:
                You.totalplus = You.totalplus + You.betAmount
                print("You won! Totalplus: ", You.totalplus)
            else:
                You.totalminus = You.totalminus + You.betAmount
                print("You lost! Totalminus: ", You.totalminus)
        
    if check() == 1:
        game()
    else:
        You.currentCard = randomCard()
        Dealer.currentCard = randomCard()

def check():
    if You.currentCard > 21: # loss
        You.totalminus = You.totalminus + You.betAmount
        print("You lost! Totalminus: ", You.totalminus)
        return 0
    elif Dealer.currentCard > 21: # win
        You.totalplus = You.totalplus + You.betAmount
        print("You won! Totalplus: ", You.totalplus)
        return 0
    elif You.currentCard == 21: #win
        You.totalplus = You.totalplus + You.betAmount
        print("You won! Totalplus: ", You.totalplus)
        return 0
    elif Dealer.currentCard == 21: #loss
        You.totalminus = You.totalminus + You.betAmount
        print("You lost! Totalminus: ", You.totalminus)
        return 0
    else: # goes on
        return 1
# Init
class Player:
    def __init__(self, currentCard, newDeal, money, betAmount, wins, totalplus, totalminus):
        self.currentCard = currentCard
        self.newDeal = newDeal
        self.money = money
        self.wins = wins
        self.totalplus = totalplus
        self.totalminus = totalminus
    def bet(self):
        self.betAmount = int(input("Bet: "))
        if (self.money - self.betAmount) < 0:
            print("You don't have enough money")
            self.bet()
        else:
            self.money = self.money - self.betAmount
    
class Dealer:
    def __init__(self, currentCard):
        self.currentCard = currentCard
        
You = Player(randomCard()[0], True, 10, 0, 0, 0, 0)
Dealer = Dealer(randomCard()[0])
# Game Loop
while True:
    print("  Money: ", You.money)
    print("  Totalplus: ", You.totalplus)
    print("  Totalminus: ", You.totalminus)
    You.bet()
    game()
    self.newDeal = true
        
        
        
    
