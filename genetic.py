import numpy as np
from case import Case
from greedy import greedy
import random
def genetic(testObject):
    initialSolution=greedy(testObject)
    if( isinstance(initialSolution[1], str) ):
        return [" "," "]
    
    Order=testObject.totalOrder
    CaseList=testObject.Cases
    firstGen=firstGeneration(CaseList,Order)
    
    
    resultCase=makeTheBinary(initialSolution[0],len(testObject.Cases))
    initialSolution[0]=resultCase
    initialSolution[1]=-1*initialSolution[1]
    firstGen.append([resultCase,findCase(CaseList,initialSolution[0]),initialSolution[1]])

    return sga(firstGen,CaseList,Order)

def sga(Generation,CaseList,Order):
    x=0
    while(x<150):
        #print(str(x)+"th step")
        Generation.sort(key=returnSecond)  
        bestTwo,selectionList=makeSelectionList(Generation)
        random.shuffle(selectionList)
        newPopulation=mating(selectionList,CaseList,Order)
        Generation=bestTwo+newPopulation
        x=x+1
    returnList= [bestTwo[0][0],bestTwo[0][2]]
    return returnList
def mating(matingPool,CaseList,Order):
    x=0
    length=len(matingPool[0][0])
    newPopulation=[]
    
    #crossing over
    while(x<9):
        crossoverPoint=np.random.randint(1,(length-1))
        newPopulation.append(matingPool[x*2][0][0:crossoverPoint]+matingPool[(x*2)+1][0][crossoverPoint:length])
        newPopulation.append(matingPool[(x*2)+1][0][0:crossoverPoint]+matingPool[x*2][0][crossoverPoint:length])
        x=x+1

    #mutation
    y=0
    leng=len(newPopulation)
    toNextGeneration=[]
    while(y<leng):
        newPopulation[y]=mutation(newPopulation[y])
        tempCase=findCase(CaseList,newPopulation[y])
        tempExcess=findExcess(Order,tempCase)
        toNextGeneration.append([newPopulation[y],tempCase,tempExcess])
        y=y+1
    return toNextGeneration

def mutation(bits):
    x=0
    length=len(bits)
    while(x<length):
        if((np.random.randint(0,100))/100<(1/length)):
            if(bits[x]=="1"):
                bits=(bits[0:x]+"0"+bits[(x+1):length])
            else:
                bits=(bits[0:x]+"1"+bits[(x+1):length])
        x=x+1
    return bits


def makeSelectionList(Generation):
    tempList=[]
    tempPercentage=[]
    selectionList=[]
    negCount=0
    sumList=sum(x[2] for x in Generation)
    for x in Generation:
        if(x[2]==-1):
            negCount=negCount+1
        else:
            tempList.append(x)
            tempPercentage.append(x[2]*100/sumList)
    bestTwo=tempList[0:2]
    x=0
    validSolutions=20-negCount     
    while(len(selectionList)<18):
        while(x==len(tempPercentage)):
            selectionList.append(tempList[0])
            if(len(selectionList)==18):
                break
        if(len(selectionList)==18):
                break
        
        frequency=tempPercentage[-1]/tempPercentage[x]
        #xe dikkat et
        while (frequency>0.5):
            selectionList.append(tempList[x])
            if(len(selectionList)==18):
                break
            frequency=frequency-1

        x=x+1

    return bestTwo,selectionList

def returnSecond(listx):
    return listx[2]    

def firstGeneration(CaseList,Order):
    
    length=len(CaseList)
    x=0
    firstGenList=[]
    flag=0
    while(x<19):
        tempBin=randomBinary(length)
        tempCase=findCase(CaseList,tempBin)
        tempExcess=findExcess(Order,tempCase)
        if(tempExcess>0):
            flag=1
        firstGenList.append([tempBin,tempCase,tempExcess])
        x=x+1
    while(flag==0):
        firstGenList.pop
        tempCase=findCase(CaseList,randomBinary(length))
        tempExcess=findExcess(Order,tempCase)
        if(tempExcess>0):
            flag=1
        firstGenList.append([tempBin,tempCase,tempExcess])
    return firstGenList

def randomBinary(length):
    x=0
    binary=""
    while(x<length):
        a=np.random.randint(0,2)
        binary=binary+str(a)
        x=x+1
    return binary

def findCase(caseList,binaryCode): #Finding total number of product in all subsets = O(n*k)
    size=len(caseList[0].productNumbers)
    caseCount=len(caseList)
    sumCase=[0]*size
    y=0
    while y<size:#product size
        x=0
        tempSum=0
        while x<caseCount:#total Cases
            tempSum=tempSum+caseList[x].productNumbers[y]*(int(binaryCode[x]))
            x=x+1
        sumCase[y]=tempSum
        y=y+1
    return(Case(0,sumCase))

def findExcess(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    
    tempList=list(np.array(totalCase.productNumbers)-np.array(totalOrder.productNumbers))
    for x in tempList:
        if x<0:
            return -1
    return sum(tempList)

def makeTheBinary(caseList,size): 
    x=0
    binaryCode=""
    while(x<size):
        if(x in caseList):
            binaryCode=binaryCode+"1"
        else:
            binaryCode=binaryCode+"0"
        x=x+1
    return binaryCode