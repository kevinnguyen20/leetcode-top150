class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        min=100000

        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            elif prices[i]>min and prices[i]-min>p:
                p=prices[i]-min
        
        return p
