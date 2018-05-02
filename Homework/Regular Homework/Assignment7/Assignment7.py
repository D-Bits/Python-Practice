#Create a tip calculator using classes
#By Dana Lockwood (11/21/17)

class tip:
    def __init__(self, amount, tips): #initialize the bill, and tip
        self.amount = amount
        self.tips = tips
        self.tipamount = 0
    def calctip(self):
        self.tipamount = self.amount * self.tips #Calculate tip amount
    def getTip(self):
        return self.tipamount
    
def main():
    amount = float(input("Please input the bill amount: ")) #Input the bill
    tippercent = float(input("Please enter tip percentage (as decimal): "))
    tax = amount * .095 #Define tax percentage
    t = tip(amount, tippercent)
    t.calctip()
    print("Your tip is: $", t.getTip()) #Print the tip total
    print("The tax amount is: $", tax) #Print the tax amount
    print("Your total bill is: $", t.getTip() + amount + tax) #Print the total bill
    print("Have a nice day")

main()
