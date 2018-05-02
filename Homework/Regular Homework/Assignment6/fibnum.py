#A program to dispaly the Fibonnaci numbers
#By Dana Lockwood (11/14/17)
 
#Input the number of operations
fibinput = int(input("Please enter the no. of operations: "))

fibtwo = 1 #Second number
fibone = 0 #First number

print(fibtwo)
print(fibone)

for i in range(fibinput):
    currentnum = fibtwo+fibone #Define the current number
    print(currentnum)
    fibtwo = fibone
    fibone = currentnum

    print()
    print()
