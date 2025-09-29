#list=  [9,-3 ,3,-5,-2 , 4,23,45,8]

#output => [9 , 4 , 23 ,45 , 8]
list = [9,-5,4,-6,7,8,-3,-2,23,-48]
a=[]

for i in range (len(list)):

    if list[i] > 0 :
        a.append(list[i])
        
print(a)