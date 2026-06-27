
def search_element_idx(nums,number):
    n = len(nums)
    
    if n == 1 and nums[0] == number:
        return 0
    
    for i in range(0,n):
        if nums[i] == number:
            return i
        
    return -1


nums = [1,0,2,4,3,0,0,3,5,1]

print(search_element_idx(nums,9))