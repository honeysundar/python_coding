#bubble sort 
list=[20,10,15,5,30]
for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
          if list[idx]>list[idx+1]:
              temp = list[idx]
              list[idx] = list[idx+1]
              list[idx+1]= temp
print(list)

#sort without functions  

#sort
num=[10,3,5,8,34]
new_list=[]

for i in range(len(num)):
    print(i)
    min=num[0]
    print("min value",min)
    for j in num:
        if j < min: 
            min = j 
    print("min",min)
    new_list.append(min)
    #print(new_list)
    num.remove(min) 
    print("num",num)
    print("new_list",new_list)
print(new_list)
