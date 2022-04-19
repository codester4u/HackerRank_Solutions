

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.res=[]
        for i in range(1,n+1):
            if n%i==0: self.res.append(i)
        return sum(self.res)    

