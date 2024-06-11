v = 'aeiouAEIOU'

count = 0
str = input("enter string:")
for i in range(len(str)):
    if str[i] in v:
        count+=1
print(count)
        