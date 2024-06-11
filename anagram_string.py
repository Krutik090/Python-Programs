str1 = input("Enter String1 :")
str2 = input("Enter String2 :")
count = 0
if len(str1) == len(str2):
    n = len(str1)
    for i in range(n):
        for j in range(n):
            if str1[i] == str2[j]:
                count = count + 1
    if count == n:
        print("Both are anagram strings")
    else:
        print("not anagram String")
else:
    print("not anagram because lenght is not same")
    