from queue import Queue
import sys

class Vault():
    #Initialize vault
    def __init__(self, chars, nums):
        #Total number of possible characters
        self.c = chars

        #Total number of digits in combo
        self.n = nums

        #Time it would take to crack vault
        self.time = self.getTimeToCrack()
    
    #Calculate time to crack vault
    def getTimeToCrack(self):
        seconds = 1

        #Create placeholder combo e.g. "0000VV" if c == 6 and n == 4
        combo = ""
        combo += "0"*self.n
        combo += "V"*(self.c-self.n)

        #Calculate number of possible combos
        for i in combo:
            if i == "0":
                #10 possible digits for each number spot
                seconds *= 10
            else:
                #5 possible vowels for each vowel spot
                seconds *= 5

        #Return seconds it would take to crack, assuming it takes one second per combo
        return seconds
    
    def __repr__(self):
        return "Vault: " + str(self.time)
        
class Robber():
    #Initialize Robber
    def __init__(self):
        #Number of seconds left to crack current vault
        self.secondsToCrack = 0
        
    #Set number of seconds to crack
    def crackVault(self, vault):
        self.secondsToCrack = vault.time
    
    def __repr__(self):
        return "Robber: " + str(self.secondsToCrack)
    
#Read in data

#Number of robbers
robberNum = int(input())

#Number of vaults
v = int(input())

#Initialize freeVaults queue
freeVaults = Queue()

#Tnitialize free robbers array (Robbers not currently working on a vault)
freeRobbers = []

#Initialize working robbers array (Robbers currently working on a vault)
workingRobbers = []

#Initialize heistTime
heistTime = 0

#Add robbers to freeRobbers array
for i in range(robberNum):
    freeRobbers.append(Robber())

#Add vaults to vaults queue
for i in range(v):
    chars, nums = [int(j) for j in input().split()]
    freeVaults.put(Vault(chars, nums))

#Calculate time of heist
while freeVaults.qsize() != 0:
    workingOnAllVaults = False

    #Reset timePassed to 0
    timePassed = 0

    #Assign free robbers to vaults
    for fr in freeRobbers:
        if freeVaults.qsize() == 0:
            workingOnAllVaults = True
            break
        fr.crackVault(freeVaults.get())
        workingRobbers.append(fr)
    freeRobbers = []

    #Sort working robbers from smallest to largest vault
    workingRobbers = sorted(workingRobbers, key = lambda x: x.secondsToCrack)

    if not workingOnAllVaults:
        #Add smallest in-progress vault's time to total time
        timePassed = workingRobbers[0].secondsToCrack
        heistTime += timePassed

        #Subtract smallest in-progress vault's time from rest of vaults
        for wr in workingRobbers:
            wr.secondsToCrack -= timePassed

        #See if any other vaults are completed and unasign any done robbers
        for wr in workingRobbers:
            if wr.secondsToCrack == 0:
                freeRobbers.append(wr)
                workingRobbers.remove(wr)

#Add largest vault's time to total time
if len(workingRobbers) > 0:
    heistTime += workingRobbers[-1].secondsToCrack

#Print time
print(heistTime)


