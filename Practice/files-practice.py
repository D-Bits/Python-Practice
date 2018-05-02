#Files

def main():
    fileName = input("Enter file name: ")
    inFile = open(fileName, "w")
    content = input("Write something ")
    print(content, file=inFile)
    inFile.close

    print("********")
    inFile = open(fileName, "r")
    #for line in inFile
    text=inFile.read()
    print (text)
    inFile.close()

main()
