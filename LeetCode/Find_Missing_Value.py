
def Find_Missing_Value(num):
    n = len(num)
    
    return ((n*(n+1))//2) - sum(num)
        
            
            
num = [1,2,0,4,5]
print(Find_Missing_Value(num))