list=[20,10,15,5,30]
for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
          if list[idx]>list[idx+1]:
              temp = list[idx]
              list[idx] = list[idx+1]
              list[idx+1]= temp
print(list)
