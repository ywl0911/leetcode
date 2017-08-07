class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])

        row = False
        column = False

        for i in range(m):
            if matrix[i][0] == 0:
                column = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                row = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if row:
            for i in range(n):
                matrix[0][i] = 0

        if column:
            for i in range(m):
                matrix[i][0] = 0
