def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
def fib(n):
    for i in range(n):
        print(i,)
        

print(fact(5))  
print(fib(5))
  