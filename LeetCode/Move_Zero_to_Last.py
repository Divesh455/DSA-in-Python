

def Move_Zero_to_last(nums):
    n = len(nums)
    if (n == 1):
        return
    
    i = 0
    while (i < n):
        if nums[i] == 0:
            break
        
        i+=1
    
    if i == n:
        return
    j = i + 1
    
    while j<n:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            
            i += 1
        
        j += 1
 


nums = [1,0,2,4,3,0,0,3,5,1]

Move_Zero_to_last(nums)

print(nums)