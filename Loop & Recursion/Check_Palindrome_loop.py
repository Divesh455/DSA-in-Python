n = 1234
num = n
res = 0

while num == 0:
    idx = num % 10
    res = (res * 10) + idx
    num = num // 10
    
if n == res:
    print(f"{n} is Palindrome")
else:
    print(f"{n} is not Palindrome")