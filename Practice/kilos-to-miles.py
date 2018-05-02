#Conversion to kilometers
#get the input in miles
#Then, calculate in miles
#finally, print the results

def getMiles():
    miles=float(input("Enter the number of miles "))
    return miles

def calc(miles):
    kilos = miles * 1.609
    return kilos

def printKs(kilos):
    print(kilos)

def main():
    mls = getMiles()
    ks = calc(mls)
    printKs(ks)

main()
