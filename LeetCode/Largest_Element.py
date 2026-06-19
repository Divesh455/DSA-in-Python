def largest(nums):
    largest = float("-inf")
    n = len(nums)
    
    for i in range(0,n - 1):
        largest = max(largest , nums[i])
    
    return largest


nums = [7,4,3,5,8,9,1]
print(largest(nums))
