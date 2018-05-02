#simple functions....again
def cube(number):
    myCube = number * number * number
    return myCube #This will pass it to the function

def getInput():
    number = int(input("Enter a number "))
    return number

def printCube(myCube):
    print ("The cube is ",myCube)

def main():
    number=getInput()
    myCube=cube(number)
    printCube(myCube)

main()

    
    
