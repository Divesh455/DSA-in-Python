def rev(nums,left,right):
    if left >= right :
        return 

    nums[left],nums[right] = nums[right],nums[left]
    
    rev(nums,left + 1, right-1)
    return nums

nums = [5,7,3,2,6,1,5,9]
print(rev(nums,0,7))