class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min_p = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]

            result = max(result, prices[i] - min_p)

        return result
