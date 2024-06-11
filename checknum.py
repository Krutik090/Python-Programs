p = 1
while p == 1:
    print("-------------------------------------------")
    print("Select the option from below")
    print(" 1.Even/Odd \n 2.Prime \n 3.palindrome \n 4.Armstrong \n 5.Krishnamurthy")
    print("-------------------------------------------")
    n = int(input("Enter number: "))
    ch = int(input("Enter your choice:"))

    if ch == 1:
        if n%2==0:
            print(n,"is Even")
        else:
            print(n,"is Odd")
    elif ch == 2:
        flag = False 
        if n == 1:  # 1 is not a prime 
            print(n,"is not a Prime number")
        elif n > 1:
            for i in range(2,n): # iterate in range of 2 to number itself
                if n % i == 0: # the factor is found not a prime 
                    flag = True #set flag true if not a prime

                break
            if flag:
                print(n,"is not prime number")
            else:
                print(n,"is a prime number")
    elif ch == 3:
        temp = n
        rev = 0
        while n > 0:
            d = n % 10
            rev = (rev*10)+d
            n = n//10
        if (rev==temp):
            print(temp,"is palindrome")
        else:
            print(temp,"is not palindrome")

    elif ch==4:
        temp = n
        arms = 0
        while n > 0:
            d = n % 10 # featch last digit d
            arms = arms +(d*d*d) #add the cube of d to armstrong
            n = n//10 #eliminate the last digit
        if arms == temp:
            print(temp,"is armstrong number")
        else:
            print(temp,"is not a armstrong number")
    elif ch==5:
        temp = n
        kris = 0
        while n > 0:
            d = n % 10 # featch last digit d
            fact = 1
            for i in range(1,d+1): # get factorial of d
                fact = fact * i
            #print(fact)
            kris = kris + fact # add fact(d) to krishnamurthy
            #print(kris)
            n = n // 10 #eliminate the last digit 
       # print(kris)
        if kris == temp:
            print(temp,"is a Krishnamurthy number")
        else:
            print(temp,"is not a Krishnamurthy number")
    p = int(input("want to check another 1 for contine 0 for exit:"))
        
        
        














        
        
        
    

