#A program to shuffle the values in a list
#By Dana Lockwood (12/17/17)

import random #Import from the "random" library

thisList = ["A","horse","jumps","over","the","fence"]

print(thisList) #First, print the sentence (list) in the correct order

random.shuffle(thisList) #Shuffle the list

print(thisList) #Now, print the list in suffled order
