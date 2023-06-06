class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float("inf")
        for i in prices:
            if low > i:
                low = i
            elif i - low > profit:
                profit = i - low
        return profit
            