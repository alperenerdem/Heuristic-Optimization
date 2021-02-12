from case import Case
import numpy
from greedy import greedy
import math


def simulatedannealing(testObject):
    initialSolution=greedy(testObject)
    if(not( isinstance(initialSolution[1], str) )):
        size=len(testObject.Cases)
        resultCase=makeTheBinary(initialSolution[0],size)
        currentExcess=initialSolution[1]
        caseList=testObject.Cases
        order=testObject.totalOrder


        Temparature=-1*currentExcess
        
       
        k=5*size
        if(k>500):
            k=500
        factor = (0.0001/Temparature)**(1/float(k))
        for i in range(k):
            Temparature=Temparature*factor
            badmoves=0
            for j in range(size):
                a,b=numpy.random.randint(0,size, size= 2)
                c,d=numpy.random.randint(0,2, size= 2)
                temp=changeTheResult(a,b,c,d,resultCase)
                tempCase=findCase(caseList,temp)
                tempExcess=findExcess(order,tempCase)
                if(tempExcess!=1):
                    if(currentExcess<tempExcess):
                        currentExcess=tempExcess
                        resultCase=temp
                        badmoves=0
                    else:
                        x=numpy.random.uniform()
                        if(badmoves>10):
                            break
                        badmoves=badmoves+1
                        if(tempExcess-currentExcess!=0 and x<numpy.exp((tempExcess-currentExcess)/Temparature)):
                            currentExcess=tempExcess
                            resultCase=temp

                            
        return [resultCase,currentExcess]
    else:
        solvedFlag=0
        return [" "," "]


def changeTheResult(case1,case2,result1,result2,current):
    temp=current[0:case1]+str(result1)+current[case1+1:]
    temp2=temp[0:case2]+str(result2)+temp[case2+1:]
    return temp2


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


def findExcess(totalOrder,totalCase):
    size=len(totalOrder.productNumbers)
    
    tempList=list(numpy.array(totalOrder.productNumbers)-numpy.array(totalCase.productNumbers))
    for x in tempList:
        if x>0:
            return 1
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
    