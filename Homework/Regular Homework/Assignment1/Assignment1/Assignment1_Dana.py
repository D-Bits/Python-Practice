#A program to convert kilometers to miles
#By Dana Lockwood (10/2)


#Define to function to convert kilometers to miles. 1 kilometer = ~0.62miles
def main():
    kilos = eval(input("Enter the number of kilometers to be converted to miles: "))
    miles = kilos * .62
    print("The distance in miles is ", miles, "miles")

main()