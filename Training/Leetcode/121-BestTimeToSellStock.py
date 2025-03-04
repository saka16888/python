class Solution:
    def maxProfit(self, prices) -> int:
        '''
        return : max(price[j]-price[i]), where j>i
        '''
        if prices is None: return 0
        min_price = float('inf')
        max_profit=0
        for i in prices:
            if (v := i - min_price) < 0:
                min_price = i
            elif v > max_profit :
                max_profit = v
        return max_profit

a=Solution()
stock=[7,1,5,3,6,4]
print(a.maxProfit(stock))
