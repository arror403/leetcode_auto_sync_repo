class ProductOfNumbers:

    def __init__(self):
        self.acc=[]

    def add(self, num: int) -> None:
        if num==0:
            self.acc=[]
        elif self.acc:
            self.acc.append(num*self.acc[-1])
        else:
            self.acc.append(num)
            
    def getProduct(self, k: int) -> int:
        if k>len(self.acc):
            return 0
        elif k==len(self.acc):
            return self.acc[-1]
        else:
            return self.acc[-1]//self.acc[-k-1]