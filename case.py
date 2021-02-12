
class Case:

    def __init__(self,caseNumber, productList):
        self.CaseNumber= caseNumber             
        self.productNumbers=productList
        self.productCount=len(productList)

    def __str__(self):
        return str(self.CaseNumber) +" "+str(self.productNumbers)