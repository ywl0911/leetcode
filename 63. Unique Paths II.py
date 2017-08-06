class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i - 1][0] == obstacleGrid[i][0] == 0 else 0

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j - 1] == obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                a = dp[i - 1][j] if obstacleGrid[i - 1][j] == obstacleGrid[i][j] == 0 else 0
                b = dp[i][j - 1] if obstacleGrid[i][j - 1] == obstacleGrid[i][j] == 0 else 0

                dp[i][j] = a + b

        return dp[m - 1][n - 1]
