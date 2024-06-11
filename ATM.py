'''
p = 1
minbal = 1000
bal = 50000
while p == 1:
    print("***********************************")
    print(" a.Credit amount \n b.Debit amount \n c.Show Balance")
    print("***********************************")

    ch = input("What do you want to perform ??(enter from a,b,c):")

    if ch == 'a':
          amt =int(input("Enter amount you want to creadit:"))
          bal = bal + amt
          print(f"you have succsefully creadited {amt} rupees in your account")
    elif ch == 'b':
        amt = int(input("Enter amount you want to debit:"))
        if amt > bal:
            print("you don't have sufficiant bal ")
        elif bal > 1000:
            bal = bal - amt
            print(f"you have debited {amt} from your account")
        else:
            print("sorry!!! you have riched the minimun amount in your account")
    else:
        print(f"Main balance is {bal}")
    p = int(input("Enter 1 for continue 0 for exit "))
'''

class ATM:

    def __init__(self):
        self.amt = 0
        self.minbal = 1000
    
    def withdraw(self):
        amt = int(input("Enter Amount to withdraw:"))
        if(self.amt - amt > self.minbal):
            self.amt -= amt
            print(f"{amt} Rs. Withraw Sccessfully")
        else:
            print(f"You have riched Your minimul amount \n Remaining Balance is : {self.amt}")
    
    def deposit(self):
        amt = int(input("Enter amount to deposit:"))
        self.amt +=amt
        print(f"{amt} Rs. Amount Deposit \n Remaining Balance is : {self.amt}")

    def showBalance(self):
        print(f"Your Current Balance is {self.amt}")

obj = ATM()
i = 1
while(i):
    print("***********************************")
    print(" a.Credit amount \n b.Debit amount \n c.Show Balance")
    print("***********************************")

    ch = input("Enter Choice from a,b,c):")
    if(ch=='a'):
        obj.deposit()
    elif(ch=='b'):
        obj.withdraw()
    elif(ch=='c'):
        obj.showBalance()
    else:
        print("Invalid Input!!!")
    
    i = int(input("Want to Continue 1(yes) 0(no)"))
    

        