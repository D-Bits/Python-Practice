#A program to convent numerical grades into letter grades
#By Dana Lockwood (10/30/17)

#Grade conversions
def conversions(score):
    grade = 0.0
    if score == 5:
        print("You're grade is an A! You're the best around!")
    elif score == 4:
        print("You're grade is a B. Well done.")
    elif score == 3:
        print("You're grade is a C. Not bad")
    elif score == 2:
        print("You're grade is a D. Better luck next time?")
    elif score == 1:
        print("You got an F. You fail at life, loser. Do the Walk of Shame from Game of Thrones...")

#Main function
def main():
    grade = int(input(("Please enter a number between 0 and 5: "))) 
    conversions(grade)

main()
    

