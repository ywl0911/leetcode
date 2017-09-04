class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(2, numRows + 1):
            temp_result = [1] * i
            for j in range(1, i - 1):
                temp_result[j] = result[i - 2][j - 1] + result[i - 2][j]
            result.append(temp_result)

        return result


s = Solution()
print(s.generate(5))
