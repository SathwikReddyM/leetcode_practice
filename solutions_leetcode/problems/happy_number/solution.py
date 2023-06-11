class Solution:
    def isHappy(self, n: int) -> bool:
        def count(n):
            ans = 0
            while n > 0:
                x = n % 10
                n = n // 10
                ans += x*x
            return ans
        na = []
        while n not in na:
            na.append(n)
            if n == 1:
                return True
            n = count(n)
            #print(n)
        return False

