#A program to calculate mile per gallon
#By Dana Lockwood (11/2/17)

def main():
    miles = int(input("Enter the no. of miles driven: "))
    gallons = int(input("Enter the no. of gallons of gas used: "))
    mileage = miles / gallons
    print("Your mileage is: ", mileage, "miles per gallon")
    
main()
