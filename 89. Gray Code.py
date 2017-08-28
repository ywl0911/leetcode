class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        result = ['0' * n]

        for i in range(1, n + 1):
            length = len(result)
            for j in reversed(range(length)):
                temp = list(result[j])
                # print temp
                temp[-i] = '1'
                result.append(''.join(temp))

        return [int(str(i), 2) for i in result]


s=Solution()
print s.grayCode(2)