num = [2,4,5,3,7,9,8,1,6]

for i in range(len(num)-1,0,-1):
    for j in range(0,i):
        if num[j] > num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
        

print(num)
      