from case import Case
from order import Order
import ast

class TestList:
    

    def __init__(self):
        self.listOfTests=[]
        self.testCount=0

    def createNewTestScenario(self,testDetails):
        tempTest=Test(testDetails)
        self.listOfTests.append(tempTest)
        self.testCount=self.testCount+1

    def testCreater(self,filename):
        f = open(filename, "r")
        Lines= f.readlines()
        lineCount=len(Lines)

        x=0
        while x<lineCount:
            if("Test" in Lines[x]):
                testDetails=[]
                stopLineCount=0
                while x<lineCount:
                    if(not ("---" in Lines[x]) ):
                        testDetails.append(Lines[x].rstrip('\n'))

                    if("--" in Lines[x]):
                        stopLineCount=stopLineCount+1
                        if(stopLineCount==2): 
                            self.createNewTestScenario(testDetails)
                            break
                    x=x+1
                    if(x==lineCount):
                        self.createNewTestScenario(testDetails)
                        break 
            x=x+1


class Test:
    
   
    def __init__(self, details):
        self.createCases(details[2:details.index("Orders:")])
        self.makeOrders(details[details.index("Orders:")+1:len(details)])
        self.testDetails=details
 
    def __str__(self):
        return (str(self.testDetails))
   
   
    def createCases(self,caseList):
        self.Cases=caseList
        for x in caseList:
            self.Cases[caseList.index(x)]=Case(caseList.index(x),ast.literal_eval(x))

    def makeOrders(self,OrderList):
        self.totalOrder=combineOrders(OrderList)
        
            
def combineOrders(OrderList):
        Orders=OrderList
        for x in OrderList:
            Orders[OrderList.index(x)]=ast.literal_eval(x)
        size=len(Orders[0])
        sumOrder=[]
        y=0
        while y<size:
            sumOrder.append(sum([x[y] for x in Orders]))
            y=y+1
        return(Order(sumOrder))
