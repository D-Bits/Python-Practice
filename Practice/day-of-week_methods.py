#Same Days of Week program, but with more methods
#Define array
#Get input
#Do the conversion number to word
#output

#This is a very OVERCOMPLICATED example

def setDays():
    dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return dayNames

def getDay():
    day = int(input("Enter a number between one and seven: "))
    return day

def getDayName(dayNumber):
    days = setDays()
    dayOfWeek = dayNames[day-1]
    return dayOfWeek

def printDay(dayName):
    print(dayName)

def main():
    days = getDay()
    weekDay = getDayName(day)
    printDay(weekDay)

main()