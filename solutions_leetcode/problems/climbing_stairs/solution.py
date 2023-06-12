import math
class Solution:
    def climbStairs(self, n: int) -> int:
        r = 0
        ans = 0
        while n >= r:
            ans += math.comb(n,r)
            n-=1
            r+=1
        return ans