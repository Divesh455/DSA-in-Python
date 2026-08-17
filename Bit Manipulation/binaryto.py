

def convert2des(x:str) -> int:
    des = 0
    powe = 0
    ind = len(x) - 1
    
    while ind >= 0:
        
        num = int(x[ind]) * (2**powe)
        des += num
        ind -= 1
        powe += 1
        
    return des

print(convert2des("1001"))