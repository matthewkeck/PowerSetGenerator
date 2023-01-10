def buildNextPowerSet(element,powerSet):
    
    for k in range(len(powerSet)):
        tempSet = powerSet[k].copy()
        tempSet.append(element)
        powerSet.append(tempSet)

    return powerSet

def itterateElements(inputSet,powerSet):
    
    for i in range(len(inputSet)):
        powerSet = buildNextPowerSet(inputSet[i],powerSet)
    

def printResult(powerSet):
    
    print("-----------------power set------------------------")
    print(powerSet)
    print("\nlength of power set = " + str(len(powerSet)))

def main(inputSet):

    powerSet = []
    tempSet = []

    powerSet.append(tempSet)
        
    itterateElements(inputSet,powerSet)
    printResult(powerSet)
    

inputSet = [-1,0,1]

main(inputSet)
