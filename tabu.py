from case import Case
import numpy as np
from greedy import greedy
import math
def tabu(testObject):

    initialSolution=greedy(testObject)
    if( isinstance(initialSolution[1], str) ):
        return [" "," "]
    resultCase=makeTheBinary(initialSolution[0],len(testObject.Cases))
    currentExcess=-1*initialSolution[1]   
    caseList=testObject.Cases
    order=testObject.totalOrder


    bestSolution=resultCase
    bestExcess=currentExcess
    localBest=resultCase
    localExcess=currentExcess

    tabuList=[]
    tabuList.append(localBest)
    x=0
    while(x<150):
        neighborhood=getNeighborhood(localBest,caseList,order,tabuList)
        if(len(neighborhood[0])==0):
            break
        neigList=neighborhood[0]
        excessList=neighborhood[1]
        localBest=neigList[0]
        localExcess=excessList[0]
        badMoves=0
        y=0
        for candidate in neigList:
            if(not(candidate in tabuList) and localExcess>excessList[y]):
                localBest=candidate
                localExcess=excessList[y]
            
            y=y+1
        if(localExcess<bestExcess):
            bestSolution=localBest
            bestExcess=localExcess
            badMoves=0
        else:
            badMoves=badMoves+1    
        if(not(localBest in tabuList ) ) :
            tabuList.append(localBest)
        if(badMoves==30):
            break               
        x=x+1
    
    return [bestSolution,bestExcess]



def getNeighborhood(resultCase,caseList,order,tabuList):

    neighborhood=[]
    excessList=[]
    neiglist=findNeighborhood(resultCase,1)
    
    x=0
    y=len(neiglist)
    while(x<y):
        tempCase=findCase(caseList,neiglist[x])
        tempExcess=findExcess(order,tempCase)
        if((tempExcess>0) and (not (neiglist[x] in tabuList) ) ):
            neighborhood.append(neiglist[x])
            excessList.append(tempExcess)
        x=x+1
    x=0
    if(len(neighborhood)==0):
        neiglist2=findNeighborhood(resultCase,2)
        x=0
        y=len(neiglist2)
        while(x<y):
            tempCase=findCase(caseList,neiglist2[x])
            tempExcess=findExcess(order,tempCase)
            if((tempExcess>0) and (not (neiglist2[x] in tabuList) ) ):
                neighborhood.append(neiglist2[x])
                excessList.append(tempExcess)
            x=x+1
        x=0
    return [neighborhood,excessList]

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
    
def findNeighborhood(solution,key):
    templist=[]
    length=len(solution)
    x=0
    if(key==1):
        while(x<length):
            
            if(solution[x]=="1"):
                templist.append(solution[0:x]+"0"+solution[(x+1):length])
            else:
                templist.append(solution[0:x]+"1"+solution[(x+1):length])    
            x=x+1
    else:
        while(x<(length-1)):
            y=x+1
            while(y<length):
                if(solution[x]+solution[y]=="00"):
                    templist.append(solution[0:x]+"1"+solution[(x+1):y]+"1"+solution[(y+1):length])
                elif(solution[x]+solution[y]=="01"):
                    templist.append(solution[0:x]+"1"+solution[(x+1):y]+"0"+solution[(y+1):length])
                elif(solution[x]+solution[y]=="11"):
                    templist.append(solution[0:x]+"0"+solution[(x+1):y]+"0"+solution[(y+1):length])
                elif(solution[x]+solution[y]=="10"):
                    templist.append(solution[0:x]+"0"+solution[(x+1):y]+"1"+solution[(y+1):length])
                y=y+1    
            x=x+1
    return templist
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


   # y=len(neiglist2)
   # while(x<y):
    #    tempCase=findCase(caseList,neiglist2[x])
    #    tempExcess=findExcess(order,tempCase)
    #    if(tempExcess>0):
     #       neighborhood.append(neiglist2[x])
     #       excessList.append(tempExcess)
     #   x=x+1