class Solution(object):
    def generate(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        if rowIndex == 0:
            return [1]
        result_now = [1]
        for i in range(2, rowIndex + 2):
            temp_result = [1] * i
            for j in range(1, i - 1):
                temp_result[j] = result_now[j - 1] + result_now[j]
            result_now = temp_result

        return result_now


s = Solution()
print(s.generate(0))
