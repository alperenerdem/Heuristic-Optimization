from case import Case
import numpy as np
from greedy import greedy

boundExcess = 0

def branchandbound(testObject):#Loop in subsets of cases = O(2^n)
    global boundExcess
    boundExcess=greedy(testObject)[1]
    length=len(testObject.Cases)
    initialBinary=""
    if(not( isinstance(boundExcess, str) )):
        boundExcess=boundExcess-1
    result=brancher([testObject,initialBinary,length,boundExcess])
    return result

def brancher(listx):
    global boundExcess
    x=findExcess(listx[0].totalOrder,findCase(listx[0].Cases,formatTheBinary(listx[1],listx[2])))
    y=findDiffer(listx[0].totalOrder,findCase(listx[0].Cases,formatTheBinary(listx[1],listx[2])))
    if ((not( isinstance(boundExcess, str) )) and ((x==-1 and y>boundExcess ) or (y>boundExcess and x >= boundExcess))):     
        if(x!=-1):
            if(x>boundExcess):
                boundExcess=x
            return [listx[0],formatTheBinary(listx[1],listx[2]),listx[2],x]
        if x==-1 and len(listx[1])<listx[2]:
            if(not( isinstance(listx[3], str) )):
                if(y>listx[3]):
                    takelistx=[listx[0],"1"+listx[1],listx[2],listx[3]]
                    nottakelistx=[listx[0],"0"+listx[1],listx[2],listx[3]]
                    right=brancher(takelistx)
                    left=brancher(nottakelistx)
                    if right[3]>left[3]:
                        return right
                    else:
                        return left
    return listx


def formatTheBinary(binaryCode,size):
    while(len(binaryCode)<size):
	    binaryCode="0"+binaryCode
    return binaryCode

def findDiffer(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    tempList=list(np.array(totalOrder.productNumbers)-np.array(totalCase.productNumbers))
    tempSum=0
    for x in tempList:
        if x<0:
            tempSum=tempSum+x
    return tempSum

def findExcess(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    
    tempList=list(np.array(totalOrder.productNumbers)-np.array(totalCase.productNumbers))
    for x in tempList:
        if x>0:
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

    #findExcess(listx[0].totalOrder,findCase(listx[0].Cases,formatTheBinary(listx[1],listx[2])))