#Guessing game assignment
#Use a psuedo-random number generator to produce a random number between 1 and 1001
#By Dana Lockwood (11/2/17)

#Get random range from Random library
from random import randrange

def getRandom():
    number = randrange(1,1001)
    return number

def getGuess():
    guess = int(input("Enter a guess between 1 and 1000: "))
    return guess

#Evalute the user's input
def evaluateGuess(guess,number):
    correct = 0
    if guess > number:
        print("Number is too high!")
    elif guess < number:
        print("The number is too low!")
    else:
        print("That works!")
        correct = 1
    return correct

def getScore(number):
    score=10
    for i in range(10):
        guess=getGuess()
        correct=evaluateGuess(guess, number)
        if correct == 1:
            break
        score=score-1
    return score

def test():
    scores=[]
    playAgain="y"
    while playAgain == "y":
        number = getRandom()
        score=getScore(number)
        score.append(score)
        print("You're score is: ", score)
        playAgain=input("Would you like to play again? y/n?")
        playAgain=playAgain.lower()
    return scores
    
def finalScores():
    scores=gamePlay()
    total=0
    average=0
    print("Your scores are: ")
    for item in scores:
        print(item)
        total += item
    average=total/len(scores)
    print ("youre average is ", average)

def main():
    test()
    finalScores()

main()
        

