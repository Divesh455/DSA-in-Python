def Second_Largest(num):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(num)
    
    for i in range(0,n-1):
        if num[i] > largest:
            s_largest = largest
            largest = num[i]
        elif num[i] > s_largest and num[i] != largest:
            s_largest = num[i]
    
    return s_largest

nums = [7,4,3,5,8,9,1]
print(Second_Largest(nums))