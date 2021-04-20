class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10**4
        maxNet = 0
        for index,item in enumerate(prices):
            if item < minPrice:
                minPrice = item
            elif item - minPrice > maxNet:
                maxNet = item - minPrice
        return maxNet
