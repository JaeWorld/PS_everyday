# Leetcode 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        ans = 0
        minPrice = prices[0]
        
        for i in range(1, n):
            if minPrice > prices[i]:
                minPrice = prices[i]
            if ans < prices[i]-minPrice:
                ans = prices[i]-minPrice
                
        return ans
            
