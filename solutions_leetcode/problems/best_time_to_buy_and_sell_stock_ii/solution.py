class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def back(x):
            while x < len(prices) - 1 and prices[x] < prices[x + 1]:
                x += 1
            return x
        mx = j = i = 0
        while i < len(prices) - 1:
            p = 0
            if prices[i] < prices[i + 1]:
                j = back(i)
                mx += prices[j] - prices[i]
                i = j
                if j >= len(prices) - 1:
                    break
            i += 1
                
        return mx