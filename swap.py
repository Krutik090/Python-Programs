#swap 2 values

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("values before swapping")
print("a=",a)
print("b=",b)

a = a + b
b = a - b
a = a - b

print("values after swapping")
print("a=",a)
print("b=",b)
