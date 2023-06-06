class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """max = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i] > max:
                    max = prices[j]-prices[i]
        return max"""
        profit = 0
        low = float("inf")
        #print(low)
        for i in prices:
            if low > i:
                low = i
                #print("1:"+str(low))
            elif i - low > profit:
                profit = i - low
                #print("2:"+str(profit))
        return profit
       