class mxlist:
    
    def __init__(self):
        self.l1=[]
        self.l2=[]
    def getdata(self):
        n=int(input("Enter how many numbers:"))
        for i in range(0,n):
            val=int(input("Enter values in list1:"))
            self.l1.append(val)
        print(self.l1)

        for i in range(0,n):
            val=int(input("Enter values in list2:"))
            self.l2.append(val)
        print(self.l2)
    def sumlist(self):
        if(sum(self.l1)>sum(self.l2)):
            print(f"{self.l1} length of this list is greater")
        else:
            print(f"{self.l2} length of this list is greater")



ob=mxlist()
ob.getdata()
ob.sumlist()     