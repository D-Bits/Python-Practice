#Code wil generate 41 prime numbers

def getNumber():
    number = int(input("Enter a number between 0 and 40: "))
    return number

def checkNumber(number):
    checkNumber = 0
    if number >=0 or number <=40:
        checkNumber = number
    else:
        checkNumber=-1
    return checkNumber
      
def getPrime(number):
    prime = number * number - number +41 
    return prime

def printPrime(prime):
    print ("The prime nubmer is: ", prime)

def main():
    num = getNumber()
    checkNum = checkNumber(num)
    #print(checkNumber)
    if checkNum  == -1:
        print("Numbers must be between 0 and 40")
        return
    prime = getPrime(num)
    printPrime(prime)

main()
