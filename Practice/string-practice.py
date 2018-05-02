#Peer Assignment 5, created by Dana and Bella (10/10)
def main():
    print("This program determines string length")

#imput a sentence
    strSentence = str(input("Enter a sentence: "))

#split the sentence
    wordList=strSentence.split()
    for str in wordList:
        print(str)

main()
