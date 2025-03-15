class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        minprice=float('inf')
        maxprofit=0

        j=0
        maxprofit=[] 
        total=0
        for i in range(1,len(prices)):
            if prices[i]>prices[j]:
                maxprofit.append(prices[i]-prices[j])
            j+=1
        for i in maxprofit:
            total+=i
        return total
                
