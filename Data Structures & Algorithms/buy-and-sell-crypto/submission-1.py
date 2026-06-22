class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowestP = prices[0]
        highestP = 0
        res = 0

        for i in range(len(prices)):
            lowestP = min(lowestP, prices[i])

            res = max(res, prices[i] - lowestP)

        return res
        
        