nums = [[5,10,8],[7,6,3],[2,1,9]]

rows = len(nums)
cols = len(nums[0])

if rows != cols:
    print("Matrix Are Not Cubic")              
else:
    for i in range(0,rows):        
        for j in range(0,cols):
            
                
            if (i + j) == (rows -1) or (i + j) == (cols -1):
                    print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
                
        print()