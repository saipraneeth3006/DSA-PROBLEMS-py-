class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval=prices[0]
        sum=0
        for i in range(1,len(prices)):
            sum=max(sum,(prices[i]-minval))
            minval=min(minval,prices[i])
        return sum