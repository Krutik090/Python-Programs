str = input("Enter String:")
sr = set(str)
#print(sr)
v = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for n in sr:
    if n in v:
        count += 1
print(count)

