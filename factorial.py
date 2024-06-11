n = int(input("enter number:"))

fact = 1
if n > 1:
    for i in range(1,n+1):
        fact = fact * (n)
        n-=1
    print(fact)
elif n == 1:
    print(fact)
elif n == 0:
    print(fact)
else:
    print("number is less then 0")
