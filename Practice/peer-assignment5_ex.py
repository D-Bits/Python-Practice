#Peer Assignment no.5
#By Dana and Bella (10/10/17)

def main ():
    strSentence = input("enter sentence")
    wordList = strSentence.split()
    counter=0
    for i in range(0,len(wordList)):
        wordLength=len(wordList[i])
        counter=counter + wordLength
    average = counter/len(wordList)
    print("The average word length is: ", average,"characters long")

main()
