#Use a "dice" class
#To create a program to roll D6 and a D20 dice

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

def main():
    again="y"
    while again=="y":
        die1=die(20) #D20 die
        die1.roll()
        die2=die(6) #D6 die
        die2.roll()
        print(die1.getValue(), die2.getValue())
        again=input("Enter 'y' to roll again...")
        
main()
        
