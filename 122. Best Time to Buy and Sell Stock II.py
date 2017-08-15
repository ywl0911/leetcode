class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        first = prices[0]
        second = -1
        result = [0]
        prices.append(0)
        for i in range(1, n + 1):
            # print first,second
            if prices[i] > prices[i - 1]:
                second = prices[i]
                continue
            else:
                if second - first > 0:
                    result.append(second - first)
                first = prices[i]
                second = -1

        return sum(result)
