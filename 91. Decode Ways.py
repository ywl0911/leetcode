class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        """

        n = len(s)
        dp = [0 for i in range(n)]

        if n == 0:
            return 0
        if s[0] == '0':
            return 0

        dp[0] = 1
        if n == 1:
            return 1

        if s[1] == '0':
            if s[0] in ['1', '2']:
                dp[1] = 1
            else:
                dp[1] = 0
        else:
            dp[1] = 2 if s[:2] <= '26' and s[1] != '0' else 1

        for i in range(2, n):
            if s[i] == '0':
                if '0' < s[i - 1] <= '2':

                    dp[i] = dp[i - 2]
                else:
                    dp[i] = 0
            elif s[i - 1] == '0':
                dp[i] = dp[i - 1]
            elif s[i - 1:i + 1] > '26':
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 2] + dp[i - 1]

        return dp[-1]


s = Solution()
print(s.numDecodings('10'))
