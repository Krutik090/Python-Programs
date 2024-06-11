n = int(input("Enter lenght of your searis: "))

n1 = int(input("Enter first number:"))
n2 = int(input("Enter Second number:"))

fib = []
temp = n1+n2
fib.append(n1)
fib.append(n2)
fib.append(temp)

for i in range(n-3):
    temp = fib[-1] + fib[-2]
    fib.append(temp)

print(fib)