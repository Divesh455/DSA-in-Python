
def merge_arr(left,right):
    res = []
    i,j = 0,0
    n,m = len(left),len(right)
    
    while i < n and j < m:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    if i < n:
        while i < n:
            res.append(left[i])
            i += 1
    
    if j < m:
        while j < m:
            res.append(right[j])
            j += 1   
            
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    
    return merge_arr(left,right)

arr = [3,2,4,6,7,1,8]

print(merge_sort(arr))