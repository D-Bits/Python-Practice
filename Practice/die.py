from random import randrange

class die:
    def __init__(self, sides): #A class variable that applies to every function in the class
        self.sides = sides #Self is used to define class level variables
        self.value=1 #The initial value of the dice is 1

    def roll(self):
        self.value = randrange(1,self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value=value