#Simple if statement

def main():
    number = int(input("Enter a number: "))
    if number > 5:
        print("The number is bigger than 5")
    elif number==5: #An elseif state in Python
        print("The number is EQUAL to 5")
    else:
        print("The number is NOT greater than 5!")

main()