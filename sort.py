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

my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)

print(new_list)
