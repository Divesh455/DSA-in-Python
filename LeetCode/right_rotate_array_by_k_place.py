

def Reverse(nums,lf,rg):
    while lf < rg:
        nums[lf],nums[rg] = nums[rg],nums[lf]
        lf += 1
        rg -= 1
        
def RightRotateArray(nums,k):
    n = len(nums)
    Reverse(nums,n-k,n-1)
    Reverse(nums,0,n-k-1)
    Reverse(nums,0,n-1)


nums = [3,9,5,6,7,2]

RightRotateArray(nums,4)
print(nums)