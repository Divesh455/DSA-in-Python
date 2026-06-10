num = [2,4,5,3,7,1,8,9,6]

for i in range(len(num)):
    min_idx = i
    for j in range(i+1 , len(num)):
        if num[j] > num[min_idx]:
            min_idx = j
    
    num[i],num[min_idx] = num[min_idx],num[i]


print(num)      