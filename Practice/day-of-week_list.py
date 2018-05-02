#Sample program for lists

def main():
    dayNames=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    day = int(input("Enter a number between one and seven"))
    dayOfWeek = dayNames[day-1]
    print(dayOfWeek)

main()
