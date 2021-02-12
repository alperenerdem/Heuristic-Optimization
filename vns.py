from case import Case
import numpy as np
from greedy import greedy
def vns(testObject):#Loop in subsets of cases = O(2^n)

    initialSolution=greedy(testObject)
    if(not( isinstance(initialSolution[1], str) )):
        resultCase=makeTheBinary(initialSolution[0],len(testObject.Cases))
        caseList=testObject.Cases
        currentCase=findCase(caseList,resultCase)
        order=testObject.totalOrder
        currentExcess=-1*initialSolution[1]
        solvedFlag=1
        resultCase
    else:
        solvedFlag=0
        return [" "," "]

    while solvedFlag==1:
        solvedFlag=0
        neigList=findNeighborhood(resultCase,1)
        length=len(neigList)
        x=0
        while x<length:
            tempCase=findCase(caseList,neigList[x])
            tempExcess=findExcess(order,tempCase)
            if(tempExcess!=-1 and tempExcess<currentExcess):
                resultCase=neigList[x]
                currentExcess=tempExcess
                currentCase=tempCase
                solvedFlag=1
            x=x+1
        if(solvedFlag==0):
            neigList=findNeighborhood(resultCase,2)
            length=len(neigList)
            x=0
            while x<length:
                tempCase=findCase(caseList,neigList[x])
                tempExcess=findExcess(order,tempCase)
                
                if(tempExcess!=-1 and tempExcess<currentExcess):
                    resultCase=neigList[x]
                    currentExcess=tempExcess
                    currentCase=tempCase
                    solvedFlag=1
                x=x+1
    
    return [resultCase,currentExcess]




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

def findExcess(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    
    tempList=list(np.array(totalCase.productNumbers)-np.array(totalOrder.productNumbers))
    for x in tempList:
        if x<0:
            return -1
    return sum(tempList)

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