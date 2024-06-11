class Money:

    def __init__(self):
        self.value = float(input("Enter Value"))
    
    def update(self):
        self.value = self.new
        return self.value
    
    def nonZero(self):
        if(self.value != 0):
            print("Non Zero") 
    def formatted(self):
        self.new = "{:,.2f}".format(self.value)
        return self.new
    
obj = Money()
obj.nonZero()
obj.formatted()
print(obj.update())