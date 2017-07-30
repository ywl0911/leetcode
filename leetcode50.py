class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x == 1:
            return 1

        sub = pow(x, n // 2)

        return sub * sub * x if n % 2 == 1 else sub * sub


s = Solution()
print(s.myPow(8.88023, 3))
