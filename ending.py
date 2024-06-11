str = input("Enter String:")

if len(str)>3:
    if str.endswith("ing"):
        str = str + "ly"
    else:
        str = str + "ing"
else:
    print("lenght is lessthen 3")

print(str)