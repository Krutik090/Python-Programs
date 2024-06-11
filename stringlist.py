l = int(input("enter number of string you want to enter:"))
strlist=[]
for i in range(l):
    str = input("enter string:")
    strlist.append(str)
print(f"List of the String {strlist}")
lenlist=[]
for n in strlist:
    strlen = len(n)
    lenlist.append(strlen)
print(f"List of the lenght list{lenlist}")
