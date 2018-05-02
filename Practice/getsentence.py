#Figure out the average length of a sentence
#Get the sentence
#split the sentence into words and get the lengths
#loop the words and get the lengths
#total thge lengths
#divide the total lengths by the number of words
#print the average

def getSentence():
    sentence=input("Enter a sentence")
    return sentence

def splitSentence():
    mySentence=getSentence()
    words=mySentence.split()
    return words

#Get the total length of the sentence
def getTotalLength():
    words=splitSentence()
    counter = 0
    for i in range(0, len(words)):
        counter += len(words[i])
    average=calcAverageWordLength(counter, len(words))
    return average

def calcAverageWordLength(total, sizeOfList):
    average = total / sizeOfList
    return average

def printAverage():
    print("The average word length in this sentence is: ", getTotalLength())

def test():
    #print(getSentence())
    #sentenceWords=splitSentence()
    #for i in range(0, len(sentenceWords)):
        #print(sentenceWords[i])
    #print(getTotalLength())
    print(getTotalLength())
        
test()

def main():
    #printAverage()

main()



