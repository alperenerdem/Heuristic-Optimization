from case import Case
from order import Order
from test import TestList
from test import Test
from bruteforce import bruteForce
from greedy import greedy
from dynamic import dynamic
from vns import vns
from simulatedannealing import simulatedannealing
from branchandbound import branchandbound
from tabu import tabu
from genetic import genetic
from matplotlib import pyplot as plt
import time


def explainBinary(binaryCode):
    size=len(binaryCode)
    x=0
    tempString=""
    while x<size:
        x=x+1
        if binaryCode[x-1]=='1':
            tempString=tempString+str(x)+" "
    return tempString

def plotgraphs(numbers,times1,times2,excess):
    plt.subplot(121)
    plt.xlabel('Test Cases')
    plt.ylabel('Seconds')
    plt.suptitle('RUNTIME')
    plt.bar(numbers, times1)

    
    plt.subplot(122)
    plt.xlabel('Test Cases')
    plt.ylabel('Seconds')
    plt.suptitle('RUNTIME')
    plt.bar(numbers, times2)

    plt.show()

    plt.subplot(121)
    plt.xlabel('Test Cases')
    plt.ylabel('Seconds')
    plt.suptitle('RUNTIME')
    plt.plot(numbers, times1)

    
    plt.subplot(122)
    plt.xlabel('Test Cases')
    plt.ylabel('Seconds')
    plt.suptitle('RUNTIME')
    plt.plot(numbers, times2)
    
    plt.show()

    plt.subplot(111)
    plt.xlabel('Test Cases')
    plt.ylabel('TabuExcess/Simulated Annealing')
    plt.suptitle('Excess Difference between Tabu Search and Simulated Annealing')
    plt.bar(numbers, excess)

    plt.show()

    plt.subplot(111)
    plt.xlabel('Test Cases')
    plt.ylabel('TabuExcess/Simulated Annealing')
    plt.suptitle('Excess Difference between Tabu Search and Simulated Annealing')
    plt.plot(numbers, excess)
    
    plt.show()





if __name__ == '__main__':
    Tests= TestList()
    Tests.testCreater("CSE624TESTSET.txt")
    x=0
    numbers=[]
    tabutimes=[]
    genetictimes=[]
    excessDifference=[]
    while(x<100):

        resultGenetic=genetic(Tests.listOfTests[x])
        print("Genetic Way -------- Test Case "+str(x)+": "+explainBinary(resultGenetic[0])+ " with excess of " + str(resultGenetic[1]))

        #resultTabu=tabu(Tests.listOfTests[x])
       
        #print("Tabu Way -------- Test Case "+str(x)+": "+explainBinary(resultTabu[0])+ " with excess of " + str(resultTabu[1]))  
        
        #resultGreedy=greedy(Tests.listOfTests[x])
        #print("Greedy Way --------- Test Case "+str(x)+": "+resultGreedy[0]+str(resultGreedy[1]))       
        
        #resultBranch=branchandbound(Tests.listOfTests[x])
        #print("BranchAndBound Way - Test Case "+str(x)+": "+explainBinary(resultBranch[1])+ " with excess of " + str(-1*resultBranch[3]) )     
       
        #resultSimulated=simulatedannealing(Tests.listOfTests[x])
        #resultSimulated[1]=-1*resultSimulated[1]
        #print("SA Way ---------- Test Case "+str(x)+": "+explainBinary(resultSimulated[0]) + " with excess of " + str(resultSimulated[1]))
       
        #resultVns=vns(Tests.listOfTests[x])
        #print("VNS Way --------------- Test Case "+str(x)+": "+explainBinary(resultVns[0]) + " with excess of " + str(resultVns[1]))      
       
        #print("Brute Force -------- Test Case "+str(x)+": "+explainBinary(bruteForce(Tests.listOfTests[x])))
        x=x+1
    

