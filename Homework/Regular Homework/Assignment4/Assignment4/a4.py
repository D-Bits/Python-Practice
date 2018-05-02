#A progragm to count the words in a sentence
#By Dana Lockwood (10/29/17)

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split(' ')
    print("You have:", len(words), "words")   

main()
