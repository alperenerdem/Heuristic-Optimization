from case import Case
import numpy as np
def bruteForce(testObject):#Loop in subsets of cases = O(2^n)
    size=2**len(testObject.Cases)
    x=0
    minExcess=-1
    minExcessIndex=""
    while x<size: #subset
        binaryCode=formatTheBinary(bin(x),len(testObject.Cases))
        totalCase=solve(testObject.Cases,binaryCode,testObject.totalOrder)
        excess=findExcess(testObject.totalOrder,totalCase)
        if((not(excess == -1)) and (minExcess== -1 or excess < minExcess)):#Comparing product numbers with order product numbers= O(n)
            minExcessIndex=binaryCode
            minExcess=excess
        x=x+1
    return minExcessIndex

def solve(caseList,binaryCode,totalOrder): #Finding total number of product in all subsets = O(n*k)
    size=len(caseList[0].productNumbers)
    caseCount=len(caseList)
    sumCase=[]
    y=0
    while y<size:#product size
        x=0
        tempSum=0
        while x<caseCount:#total Cases
            tempSum=tempSum+caseList[x].productNumbers[y]*(int(binaryCode[x]))
            x=x+1
        sumCase.append(tempSum)
        y=y+1
    return(Case(0,sumCase))

def findExcess(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    tempList=list(np.array(totalCase.productNumbers)-np.array(totalOrder.productNumbers))
    for x in tempList:
        if x<0:
            return -1
    return sum(tempList)

def formatTheBinary(binaryCode,size): 
    binaryCode=binaryCode[2:]
    while(len(binaryCode)<size):
	    binaryCode="0"+binaryCode
    return binaryCode