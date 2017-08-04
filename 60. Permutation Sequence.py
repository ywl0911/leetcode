class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        math.factorial(2)
        nums = list(range(1, n + 1))

        index = 0
        result = []
        for i in reversed(range(1, n + 1)):
            temp_result = 0
            for j in range(len(nums)):
                index = math.factorial(i - 1) * (j + 1)
                if k <= index:
                    temp_result = nums[j]
                    break
            # 第一位加到结果之中
            result.append(temp_result)

            index = math.factorial(i - 1) * (j)
            k = k - index
            nums.remove(nums[j])

        return result


s = Solution()
print(s.getPermutation(1, 1))
