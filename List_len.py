n = int(input("Enter length of your list:"))
str_list = []
for i in range(n):
    str1 = input("Enter String:")
    str_list.append(str1)
print(str_list)

len_list = []
for n in str_list:
    str_len = len(n)
    len_list.append(str_len)
print(len_list)

bool_list = []
for i in range(len(str_list)):
    if len(str_list[i]) == len_list[i]:
        bool_list.append(True)
        
    else:
        bool_list.append(False)
print(bool_list)
    
        
    

