'''a.	Reverse the string
b.	Find Specific Character Occurrence
c.	Replace the original string with sub string
'''

n = 1
while n==1:
    print("==============================================")
    print("a. Reverse the string ")
    print("b. Find the specific chracter Occurance")
    print("c. Replace the original string with sub string")
    str1 = input("Enter the string : ")
    ch = input("What do you want to perform with String :")
    
    
    if ch == 'a':
        print(str1[::-1])    
    elif ch == 'b':
        char = input("Enter character :")
        count = 0
        for i in range(len(str1)):
            
            if str1[i]==char:
                count += 1
        print(count)
    elif ch == 'c':
        old_str = input("what substring do you want to replace: ")
        new_str = input("Enter new substring :")
        sub_str = str1.replace(old_str,new_str)
        print(sub_str)
    else:
        print("Invalid Input Choose from(a,b,c)")
    n = int(input("Do you want to continue (1) for yes (0) for exit: "))
        
