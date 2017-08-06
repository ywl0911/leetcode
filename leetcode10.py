class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[False for col in range(len(p) + 1)] for row in range(len(s) + 1)]

        dp[0][0]=True
        for j in range(len(p)):
            if p[j] == '*' and dp[0][j - 1]:
                dp[0][j + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):

                if p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':
                    # 分两种情况讨论
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        # 这种情况a*当做空
                        dp[i + 1][j + 1] = dp[i+1][j - 1]
                    elif p[j - 1] == s[i ] or p[j - 1] == '.':
                        # 1  a*当做a
                        one = dp[i + 1][j]
                        # 2  a*当做 null
                        two = dp[i + 1][j - 1]
                        # 3  a*当做a...a
                        three = dp[i][j + 1]
                        dp[i + 1][j + 1] = one or two or three

        return dp[len(s)][len(p)]





a=Solution()
print(a.isMatch(s="",p=".*"))

