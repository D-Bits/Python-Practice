from CardClass import Card

class deck:
    def __init__(self):
        self.cards=[]
        self.populateDeck()

    def populateDeck(self):
        suits=["h","d","c","s"]
        for s in suits: #"s" represents the suit of cards
            for i in range(1,14): #"i" represents 1
                card=Card(i,s)
                self.cards.append(card)

    def getDeck(self):
        return self.cards

def main():
    d=deck()
    myDeck=d.getDeck()
    for c in myDeck:
        print(c)

main();
