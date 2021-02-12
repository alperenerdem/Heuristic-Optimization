from case import Case
from order import Order
import numpy as np
def greedy(testObject):#Loop in subsets of cases = O(2^n)
    sorteds=sortCasesAccordingProducts(testObject)
   
    newOrder=Order(testObject.totalOrder.productNumbers)
    selectedCases=[]
    length=len(testObject.Cases)
    x=0
    solved= -1
    while(x<length and solved == -1):
        bestCase=findNextBestCase(newOrder,sorteds,selectedCases)
        selectedCases.append(bestCase)
        solved = findExcess(newOrder,testObject.Cases[bestCase])
        tempList=list(np.array(newOrder.productNumbers)-np.array(testObject.Cases[bestCase].productNumbers))
        newOrder=Order(tempList) 
        x=x+1
    selectedCases.sort()
    if solved==-1:
        return [" " ," "]
    else:
        return [selectedCases,solved]

def findNextBestCase(Order,Lists,selectedCases):
    maxProduct=max(Order.productNumbers)
    maxIndex=Order.productNumbers.index(maxProduct)
    y=len(Lists[0])
    x=0
    validValue=-1
    tempMax=-1
    while x<y:
        if not(Lists[maxIndex][x].CaseNumber in selectedCases):
            validValue=Lists[maxIndex][x].CaseNumber
            if maxProduct<Order.productNumbers[maxIndex]:               
                return validValue
        x=x+1
    return validValue    




def sortCasesAccordingProducts(testObject):
    sortedLists=[]
    y=len(testObject.Cases[0].productNumbers)
    count=0
    while count<y:
        sortedLists.append(sorted(testObject.Cases, key=lambda x: x.productNumbers[count]))
        count=count+1
    return sortedLists

def findExcess(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    tempList=list(np.array(totalOrder.productNumbers)-np.array(totalCase.productNumbers))
    for x in tempList:
        if x>=0:
            return -1
    return sum(tempList)

def newCase(caseList,selectedCases,totalOrder): #Finding total number of product in all subsets = O(n*k)
    size=len(caseList[0].productNumbers)
    caseCount=len(selectedCases)
    sumCase=[]
    y=0
    while y<size:#product size
        x=0
        tempSum=0
        while x<caseCount:#total Cases
            
            tempSum=tempSum+caseList[selectedCases[x]].productNumbers[y]
            x=x+1
        sumCase.append(tempSum)
        y=y+1
    return(Case(0,sumCase))