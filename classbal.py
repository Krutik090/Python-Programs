
class BankAccount:
    def __init__(self):
        self.bal = 0
        self.min = 1000
    def deposit(self):
        amt = int(input("Enter Amount of Deposit: "))
        self.bal = self.bal+amt
            
    def withdraw(self):
        amt = int(input("Enter Amount of withdraw: "))
        if(self.bal - amt > self.min):
            self.bal = self.bal-amt
        else:
            print("You have Riched your minimum bal")
                        
    def disp(self):
        print("Your balance is",self.bal)
n = 1
while(n == 1):
    ac1 = BankAccount()
    ac1.deposit()
    ac1.withdraw()
    ac1.disp()
    n = int(input("Do you want to Continue (0) for exit (1) for continue :"))
        
