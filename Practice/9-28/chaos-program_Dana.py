#Chaos program, (in chapter 1) desgined to show how chaotic results can arise from simple starting conditions
#By Dana Lockwood (9/28/17)

def main():#define the function
    print("This program illustrates a chaotic function")
    x=eval(input("Enter a number between zero and 1"))
    for i in range(10):
        x=3.9 * x * (1-x) #define the equation
        print(x)

main()
