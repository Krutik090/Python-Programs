str = input("enter String:")
n = len(str)
l = []
'''
for i in range(n):
    if str[i] not in l:
        count = 0
        l.append(str[i])
        for j in range(n):
            if str[i] == str[j]:
                count += 1
        print(f"{str[i]} occurs {count} times")
    
'''
d ={}
for i in range(n):
    if str[i] not in d:
        d[str[i]]=1
    else:
        d[str[i]]+=1

print(d)