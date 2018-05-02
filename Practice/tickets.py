
def getSpeedLimit():
    limit = int(input("Enter speed limit: "))
    return limit

def getSpeed():
    speed = int(input("Enter the speed traveled: "))
    return speed

def determineFine(limit, speed):
    penaltyPerMPH=5
    fine=0
    if speed > limit:
        over = speed-limit
        fine = over *penaltyPerMPH
        if fine > 200:
            fine=200
        return fine

def ticket(fine):
    if fine > 0:
        print("You owe", fine, "for speeding")
    else:
        print("Thanks for visiting")

def main():
    proceed="y"
    while proceed=="y":
        limit= getSpeedLimit()
        speed = getSpeed()
        fine = determineFine(limit, speed)
        ticket(fine)
        proceed=input("Continue y/n")
        proceed.lower()

main()
        
