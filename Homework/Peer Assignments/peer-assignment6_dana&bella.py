#A program to calculate weekly gross earnings
#By Dana and Bella (10/24/17)

def main():
    getHours = int(input("Enter number of hours worked: "))
    getPay = int(input("Enter hourly pay rate: "))

    if getHours <= 40:
        weeklyEarnings = getHours * getPay
        print("Your weekly earnings are: $", weeklyEarnings)

    #if overtime is worked
    else:
        extraHours = (getPay * 1.5) * (getHours - 40)
        weeklyEarnings = (getPay * 40) + extraHours
        print("Your weekly earnings (with overtime) are: $", weeklyEarnings)

main()