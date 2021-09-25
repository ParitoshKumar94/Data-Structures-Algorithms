# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_p=0
        min_p=prices[0]
        for i in range(1,len(prices)):
            max_p=max(max_p,prices[i]-min_p)
            min_p=min(min_p,prices[i])
            
        return max_p