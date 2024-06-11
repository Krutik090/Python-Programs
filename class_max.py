class max3:
    def __init__(self,a,b,c): #initialation
        self.n1 = a #instance level attributes 
        self.n2 = b
        self.n3 = c
    def maxof3(self):
        if self.n1 > self.n2:
            if self.n1 > self.n3:
                return self.n1
            else:
                return self.n3
        elif self.n2 > self.n3:
            return self.n2
        else:
            return self.n3

num1 = max3(12, 6, 33)
print(num1.maxof3())
    
        