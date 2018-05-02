#A program to convert parsecs to light years
#By Dana Lockwood (10/5)


#Define to function to convert parsecs to light years. 1 parsec = 3.26ly
def main():
    parsecs = eval(input("Enter the number of parsecs to be converted to light years"))
    ly = parsecs * 3.26
    print("The distance in light years is ", ly, "ly")

main()
