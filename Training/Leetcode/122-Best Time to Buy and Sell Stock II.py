class Solution:
    def maxProfit(self, prices) -> int:
        '''
        return : max(price[j]-price[i]), where j>i
        '''
        if prices is None: return 0
        max_profit=0
        for i in range(1,len(prices)):
            if (v := prices[i] - prices[i-1]) > 0:
                max_profit += v
        return max_profit

a=Solution()
stock=[7,1,5,3,6,4]
print(a.maxProfit(stock))
