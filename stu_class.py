class student:
    
    def __init__(self):
        
        self.stuid = ""
        self.stuname = ""
        self.sub1 = 0
        self.sub2 = 0
        self.total = 0
        self.per = 0
    
    def getstudetail(self):
        
        self.stuid = input("Enter Student id : ")
        self.stuname = input("Enter Student name :")
        self.sub1 = int(input("Enter Sub1 Marks :"))
        self.sub2 = int(input("Enter Sub1 Marks :"))
                
        
    def sturesult(self):
        self.total = self.sub1 + self.sub2
        self.per = self.total / 2
        
    def disp(self):
        print(f"Total marks and percentange of {self.stuname} is {self.total} and {self.per}")
    
stu1 = student()
stu1.getstudetail()
stu1.sturesult()
stu1.disp()