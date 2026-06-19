def partition(num,low,high):
    pivot = num[low]
    i = low
    j = high
    
    while i < j:
        while num[i] <= pivot and i <= high - 1:
            i += 1
        
        while num[j] >= pivot and j >= low + 1:
            j -= 1
            
        if i < j:
            num[i],num[j] = num[j],num[i]
    
    num[low],num[j] = num[j],num[low]
    
    return j

def quick_sort(num, low, high):
    if low < high:
        p_idx = partition(num,low,high)
        quick_sort(num,low,p_idx - 1)
        quick_sort(num,p_idx + 1, high)
    
    return num
        
        
num = [4,6,8,9,3,2,1,7]     
n = len(num)   
  
print(quick_sort(num,0,n-1))
