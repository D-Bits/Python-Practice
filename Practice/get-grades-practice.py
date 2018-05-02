#Grade scores between 0 anmd 100
#Divide into a 4-point system

#input the score
def getScore():
    score = int(input("Enter test score: "))
    return score

#determine grading standards
def getGrade(score): 
    grade = 0.0
    if score >= 90:
        grade = 4.0 
        print("YOU'RE THE BEST AROUND! NOTHINGS GONNA EVER KEEP YOU DOWN!")
    elif score >= 85: 
        grade = 3.5
        print("Well done!")
    elif score >= 80: 
        grade = 3.0
        print("Not bad")
    elif score >= 75:
        grade = 2.5
        print("Good enough...")
    elif score >= 70:
        grade = 2.0
        print("Ok, I guess")
    elif score >= 65:
        grade = 1.0
        print("Better luck next time?")
    else:
        grade = 0.0
        print("Seriously?!? WTF?!? YOU FAIL AT LIFE LOSER! SHAME! SHAME! SHAME!")

    return grade

def printGrade(grade):
    print("Your grade is: ", grade)

def main():
    testScore = getScore()
    gradePoint = getGrade(testScore)
    printGrade(gradePoint)

main()


