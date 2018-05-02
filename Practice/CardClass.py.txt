#Card
class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
        self.value=0
        
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        if self.rank > 10:
            self.value=10
        else:
            self.value=self.rank
        return self.value
    
    def __str__(self):
        self.name=""
        su=""
        if self.suit =="d":
            su="diamonds"
        elif self.suit=="h":
            su="hearts"
        elif self.suit=="s":
            su="spades"
        else:
            su ="clubs"
        if self.rank >1 and self.rank< 11:
            self.name=str(self.rank) + " of " + su
        if self.rank==1:
            self.name="the ace of " + su
        if self.rank==11:
            self.name="the jack of " + su
        if self.rank==12:
             self.name="the queen of " + su
        if self.rank==13:
             self.name="the king of " + su
        return self.name
        
        
def main():
    
    c=Card(13,"h")
    print(c)
    print(c.getValue())

main()