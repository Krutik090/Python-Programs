n= int(input("enter lenght of list"))
l = []
for i in range(n):
    n1 = int(input("enter a number:"))
    l.append(n1)
odd=[]
for n in l:
    if n % 2!= 0:
        odd.append(n)
print(odd)
print(max(odd))
print(min(odd))