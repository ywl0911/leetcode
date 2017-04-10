import copy

import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        result = []
        total = len(s)
        for i in range(numRows):
            temp_result = []
            n = 0

            while (2 * numRows - 2) * n + i < total:
                temp_result.append((2 * numRows - 2) * n + i)
                n = n + 1
            result.append(temp_result)
        pass
        result_copy = copy.deepcopy(result)
        cha = 2 * numRows - 4
        for i in range(len(result_copy)):
            if i in [0, len(result_copy) - 1]:
                continue

            for j in range(len(result_copy[i])):
                if result_copy[i][j] + cha < total:
                    result[i].insert(2*j + 1, result_copy[i][j] + cha)
            cha = cha - 2
        pass

        result_last=[]
        for i in result:
            result_last+=i
        pass
        return ''.join(np.array(list(s))[np.array(result_last)])
s = Solution()
print((s.convert('123456789012345', 3)))
