n = 153
num = n
total = 0
le = len(str(n))
while num > 0:
    ld = num % 10
    total = total + (ld ** le)
    num = num // 10
    
if n == total:
    print(f"{n} is Almstrong")
else:
    print(f"{n} is not Almstrong")