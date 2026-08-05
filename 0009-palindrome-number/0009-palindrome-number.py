class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        res = 0
        while(num>0):
            LD = num % 10
            res = (res * 10) + LD
            num = num // 10
        return x == res