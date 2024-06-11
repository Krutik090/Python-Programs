n = 1
my_tuple = tuple(input('Enter space-separated words: ').split())
print(my_tuple)
while n ==1:
    print("===========================================")
    print("a. Add an element to tuple ")
    print("b. Count perticular element in tuple")
    print("c. Reverse a tuple")
    
    
    ch = input("what do you want to perform ? :")

    if ch == 'a':
        ele = input("Enter element you want to Insert: ")
        my_tuple = my_tuple + (ele,)
        print(my_tuple)
    elif ch == 'b':
        ele = input("Enter element you want to count:")
        count = 0
        for i in my_tuple:
            if i == ele:
                count+= 1
        print(f"Total number of element {ele} is :",count)
    elif ch == 'c':
        rev_tuple = my_tuple[::-1]
        print(my_tuple)
        print("Revsersed tuple is",rev_tuple)
    else:
        print("Invalid Input Enter from(a,b,c)")
    
    n = int(input("Do you want to continue (1) for yes (0) for no:"))
        

