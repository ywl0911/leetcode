class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        import copy
        r = copy.deepcopy(matrix)
        A = len(matrix)

        for i in range(A):
            for j in range(A):
                r[j][- i - 1] = matrix[i][j]

        for i in range(A):
            for j in range(A):
                matrix[i][j] = r[i][j]

        return matrix


s = Solution()
print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
