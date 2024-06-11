str = input("Enter String:")
cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n=len(str)
for i in range(0,n):
    if str[i] in cap :
        print(str.index(str[i]))