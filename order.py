
class Order:


    def __init__(self,productList):  
        self.productNumbers=productList

        self.productCount=len(productList)



    def __str__(self):
        return str(self.productNumbers)