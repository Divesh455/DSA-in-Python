class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        cnt = 0

        for i in range(0,32):
            if ans & (1<<i) != 0:
                cnt += 1
        
        return cnt