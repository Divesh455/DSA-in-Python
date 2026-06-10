nums = [5,7,3,2,6,1,5,9]

l = 0
r = 7

while(l < r):
    nums[l],nums[r] = nums[r],nums[l]
    
    l += 1
    r -= 1
    
print(nums)