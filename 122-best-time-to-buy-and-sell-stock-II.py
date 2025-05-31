class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum=0
        p=0
        min=10000

        if len(prices)==1:
            return 0

        min=prices[0]

        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                sum+=p
                p=0
                min=prices[i]
            elif prices[i]>min:
                p=prices[i]-min
            elif prices[i]<min:
                min=prices[i]
            
            if i==len(prices)-1:
                sum+=p
        return sum
