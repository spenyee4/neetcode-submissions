class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxMoney = 0
        left = 0

        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right
            elif prices[left] < prices[right]:
                currMoney = prices[right] - prices[left]
                maxMoney = max(maxMoney, currMoney)
        
        return maxMoney