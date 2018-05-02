#A program to create a deck of cards
#By Dana Lockwood (11/16/17)

#Define card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank #Which number of card in the deck
        self.suit = suit
        self.value = 0 

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        if self.rank > 10:
            self.value = 10
        else:
            self.value = self.rank
        return self.value

    def __str__(self):
        self.name=""
        su = ""
        if self.suit == "d":
            su = "Diamond"
        elif self.suit=="h":
            su="Hearts"
        elif self.suit=="s":
            su= "Spades"
        else:
            su = "Clubs"
        if self.rank < 11:
            self.name=str(self.rank) + " of " + su
        if self.rank==1:
            self.name="The Ace of " + su
        if self.rank==11:
            self.name="The jack of " + su
        if self.rank==12:
            self.name="The Queen of " + su
        if self.rank == 13:
            self.name ="The King of " + su
        return self.name

def main():
    c=Card(1, "s")
    print(c)

main()