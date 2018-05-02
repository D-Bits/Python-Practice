#Miles per gallon calculator 
#Using classes

class Mileage:
    def __init__(self, miles, gallons):#initilize params
        self.miles = miles
        self.gallons=gallons

    def setMiles(self, miles):
        self.miles = miles

    def mpg(self):
        self.milesPerGallon = self.miles / self.gallons
        return 

    def getMPG(self):
        return self.milesPerGallon

    def __str__(self):
        self.mpg()
        return "Your mpg is: " + str(self.getMPG())        

def main():
    mls = float(input("How many total miles?: "))
    gals = float(input("How many gallons?: "))
    mileage = Mileage(mls, gals)
    print(mileage)

main()