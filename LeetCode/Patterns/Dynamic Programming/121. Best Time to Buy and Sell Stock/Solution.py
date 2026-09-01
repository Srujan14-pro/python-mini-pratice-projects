class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        maxprofit=0
        for price in prices:
            if price<mini:
                mini=price
            maxprofit=max(maxprofit,price-mini)
        return maxprofit 
        


        