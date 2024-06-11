#5.	Take three subject marks as user entry and then calculate percentage and display the class, “Distinction”, “First”, “Second” and so on.
m1 = int(input("Maths Marks :"))
m2 = int(input("Science Marks :"))
m3 = int(input("English Marks :"))

total = m1+m2+m3

per = total/3 

if(per>80):
    print("distinction")
elif(per>70):
    print("Firstclass")
elif(per>48):
    print("Secondclass")
elif(per>33):
    print("Passclass")
else:
    print("FAIL")