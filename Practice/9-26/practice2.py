#Program to do a simple calculation
#By Dana Lockwood 9/26/17

def main(): #Evaluate the string to see if it can be converted to a number
    #number=eval(input("Enter a number from 1 to 41"))
    for number in range(1,40): #Will print 40 prime numbers, starting from 41
        prime=number * number-number + 41
        print(prime)

main()
