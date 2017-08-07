class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        k = len(nums)
        if k == 0:
            return []
        for i in range(2 ** k):
            temp_str = bin(i).replace('0b', '')
            temp_result = []

            for j_index, j in enumerate(temp_str[::-1]):
                if j == '1':
                    temp_result.append(nums[-j_index])

            result.append(temp_result)

        return result