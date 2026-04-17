class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        maxSoFar = 0
        while r < len(prices) - 1:
            maxSoFar = max(maxSoFar, prices[r] - prices[l])
            if prices[r] - prices[l] < 0:
                l = r
            r += 1
        maxSoFar = max(maxSoFar, prices[r] - prices[l])
        return maxSoFar
            
        
            
                
            