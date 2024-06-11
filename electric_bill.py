l = [[1,"krutik",["jan",500],["feb",900],["march",1200]]]

read_list = []

for i in range(5):
    for j in range(5):
        for k in range(5):
            if i == 0 and j > 1 and k == 1:
                read_list.append(l[i][j][k])
print(read_list)        


    
    
